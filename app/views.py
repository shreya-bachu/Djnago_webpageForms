from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO .is_valid():
            tname=TFDO.cleaned_data['tname']
            LTO=topic.objects.get_or_create(tname=tname)
            if LTO[1]:
                return HttpResponse('New topic is created...')
            else:
                return HttpResponse('Topic is already exits...')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=WebForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebForm(request.POST)
        if WFDO .is_valid():
            tname=WFDO.cleaned_data['tname']
            name=WFDO.cleaned_data['name']
            email=WFDO.cleaned_data['email']
            url=WFDO.cleaned_data['url']
            TO=topic.objects.get_or_create(tname=tname)
            LWO=webpage.objects.get_or_create(tname=TO,name=name,email=email,url=url)
            if LWO[1]:
                return HttpResponse('New Webpage is created...')
            else:
                return HttpResponse('Webpage is already exits...')
    return render(request,'insert_webpage.html',d)
# Create your views here.
