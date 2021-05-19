# This file is created manually by kapil
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse('''<h1> Home Page </h1> <a href="https://www.facebook.com/"> Facebook </a> 
    # </h1> &nbsp&nbsp <br> <a href="https://www.instagram.com/"> Instagram </a> ''')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text','default')      # text and removepunc variable value will come from index.html

    #checking checkbox values
    removepunc = request.POST.get('removepunc', 'off') 
    fullcaps = request.POST.get('fullcaps', 'off') 
    newlineremovar = request.POST.get('newlineremovar', 'off') 
    spaceremover = request.POST.get('spaceremover', 'off') 
    extraspaceremover = request.POST.get('extraspaceremover', 'off') 
    charCount = request.POST.get('charCount', 'off') 
    # analyzed = ""

    #check which checkbox is on
    if removepunc == "on": # means you hit the checkbox button
        # Analyze the text
        # return HttpResponse('''Remove punch <br> <a href="http://127.0.0.1:8000/" > Home </a> ''')
        # analyzed = djtext
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char 
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed} # purpose and analyzed_text will be replaced in analyze.html sheet
        djtext = analyzed
        # print('text from removepuch: ',djtext)
        # return render(request, 'analyze.html',params) # two parameter passed here purpose and analyzed_text
        ## bug when the text "this;is" is given in the browser with remove punctuation option it results in removal of newline
        # character, this is due to nature of html to avoid this will have to use "pre tags"
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to uppercase', 'analyzed_text':analyzed} # purpose and analyzed_text will be replaced in analyze.html sheet
        # return render(request, 'analyze.html',params)
        djtext = analyzed
        # print('text from analyzed: ',djtext)
    
    # new line character remover
    if(newlineremovar == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r": #carriage return
                analyzed = analyzed + char
        params = {'purpose':'Removed New lines', 'analyzed_text':analyzed} # purpose and analyzed_text will be replaced in analyze.html sheet
        djtext = analyzed
        # return render(request, 'analyze.html',params)
    
   
    if(spaceremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !=" ":
                analyzed = analyzed + char
        params = {'purpose':'Space from text Removed', 'analyzed_text':analyzed} # purpose and analyzed_text will be replaced in analyze.html sheet
        djtext = analyzed
        # return render(request, 'analyze.html',params)
    
    
    if(extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose':'Extra space from text Removed', 'analyzed_text':analyzed} # purpose and analyzed_text will be replaced in analyze.html sheet
        djtext = analyzed
        # return render(request, 'analyze.html',params)

    if(charCount == "on"):
        analyzed = ""
        # count = 0
        # print('Text received: ',djtext)
        for char in djtext:
             if char !="\n":
                analyzed = analyzed + char
        # print('len analyzed:',len(analyzed))
        # print('length djtext:',len(djtext))
        params = {'purpose':'Character count is', 'analyzed_text':len(analyzed)} # purpose and analyzed_text will be replaced in analyze.html sheet
        djtext = analyzed
        # return render(request, 'analyze.html',params)

    # else: # if removepunc is off
    #     return HttpResponse('''Error! Check the checkbox for removepunc to proceed <br> <a href="http://127.0.0.1:8000/" > Home </a> ''')
    if(removepunc == 'off' and fullcaps == 'off' and newlineremovar == 'off' and  spaceremover == 'off' and 
    extraspaceremover == 'off' and charCount == 'off'):
     return HttpResponse('''Error! Check the checkbox for Text Analyser to proceed <br> <a href="http://127.0.0.1:8000/" > Home </a> ''')
    
    return render(request, 'analyze.html',params)

## About US
def about(request):
    return render(request, 'about.html')

# def analyze(request):
#     return HttpResponse("Capatilise First")