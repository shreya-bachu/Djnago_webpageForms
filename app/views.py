from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
from django.http import HttpResponse

def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            topic_name=TFDO.cleaned_data['topic_name']
            LTO=topic.objects.get_or_create(topic_name=topic_name)
            if LTO[1]:
                return HttpResponse('New Topic is Created')
            else:
                return HttpResponse('Topic Is Already present')
        else:
            return HttpResponse('Invalid data')
    return render(request,'insert_topic.html',d)



def insert_topic_modelform(request):
    ETMFO=TopicModelForm()
    d={'ETMFO':ETMFO}
    if request.method=='POST':
        TMFDO=TopicModelForm(request.POST)
        if TMFDO.is_valid():
            TMFDO.save()
            return HttpResponse('Topic is Created')
        else:
            return HttpResponse('Invalid Data')


    return render(request,'insert_topic_modelform.html',d)


def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}

    if request.method=='POST':
        WDFO=WebpageForm(request.POST)
        if WDFO.is_valid():
            topic_name=WDFO.cleaned_data['topic_name']
            name=WDFO.cleaned_data['name']
            print(name)
            url=WDFO.cleaned_data['url']
            email=WDFO.cleaned_data['email']
            TO=topic.objects.get(topic_name=topic_name)
            WO=webpage.objects.get_or_create(topic_name=TO,name=name,email=email,url=url)

            if WO[1]:
                return HttpResponse('Webpage is created')
        else:
            return HttpResponse('InValid Data')
            
    return render(request,'insert_webpage.html',d)

def insert_webpage_modelform(request):
    EWMFO=WebpageModelForm()
    d={'EWMFO':EWMFO}

    if request.method=='POST':
        WDMFO=WebpageModelForm(request.POST)
        if WDMFO.is_valid():
            WDMFO.save()
            return HttpResponse('Webpage  is created')
        else:
            return HttpResponse('Invalid Data')

    return render(request,'insert_webpage_modelform.html',d)

















