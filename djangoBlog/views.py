from django .shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    #return HttpResponse('hi there! im hello  word!')
    return render(request, 'About.html')

def home(request):
    #return HttpResponse('ILOVE YOU ALI RANJBAR')
    return render(request,'Home.html')
