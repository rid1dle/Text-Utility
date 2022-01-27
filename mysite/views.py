import django
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request):
    prams = {'name': 'Himanshu', 'place': 'Mars'}
    return render(request, 'index.html', prams)


def analyse(request):

    def isAnalysedEmpty(analysed, djtext):
        if analysed == "":
            return djtext
        else:
            return analysed

    # Get the text
    djtext = request.POST.get('text', 'Seems like no text was inserted')

    # Get all the check marks
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    analyse = ""
    if removepunc == 'on':
        pur = "Remove Punctuations"
        # Analyse the text
        punctuations = '''!()-[]}{;:'"\,<>./?@#$%^&*_~'''
        for i in djtext:
            if i not in punctuations:
                analyse += i
        analysed = analyse

    if (fullcaps == 'on'):
        analysed = isAnalysedEmpty(analyse, djtext)
        analyse = ""
        analyse = analysed.upper()
        pur = "Changed to upper case"
        analysed = analyse

    if (newlineremover == 'on'):
        analysed = isAnalysedEmpty(analyse, djtext)
        analyse = ""
        pur = "Removes all the New lines"
        for i in analysed:
            if i != '\n' and i != '\r':
                analyse += i
        analysed = analyse

    if (extraspaceremover == 'on'):
        analysed = isAnalysedEmpty(analyse, djtext)
        analyse = ""
        pur = "Extra Space Remover"
        for i in range(len(analysed)):
            if analysed[i] == " " and analysed[i + 1] == " ":
                continue
            else:
                analyse += analysed[i]
        analysed = analyse

    if (removepunc == 'off' and fullcaps == 'off' and newlineremover == 'off' and extraspaceremover == 'off'):
        return HttpResponse("Seems Like You Didn't wanna know this")

    prams = {'purpose': pur,
             'analysed_text': analysed}
    return render(request, 'analyse.html', prams)
