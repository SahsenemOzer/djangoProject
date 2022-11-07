from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    text="Merhaba Şahsenem"


    context = {'text':text}
    return render(request,'index.html',context)