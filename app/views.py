from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *

def first(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        print(username)
        print(password)
        return HttpResponse('<center><h1>Data is Submitted</h1></center>')
    return render(request,'first.html')


def insert_topic(request):
    if request.method=='POST':
        topic=request.POST['topic']

        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('<center><h1>Insertion of Topic is Done</h1></center>')

    return render(request,'insert_topic.html')

def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        topic=request.POST['topic']
        nam=request.POST.get('nam')
        ur=request.POST['ur']
        TO=Topic.objects.get(topic_name=topic)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=nam,url=ur)[0]
        WO.save()
        return HttpResponse('<center><h1>Insertion of Webpage is Done</h1></center>') 
    return render(request,'insert_webpage.html',d)   

def insert_accessrecord(request):
    LWO=Webpage.objects.all()
    wd={'LWO':LWO}
    if request.method=='POST':
        #topic=request.POST['topic']
        nam=request.POST['nam']
        dat=request.POST['dat']
        aut=request.POST['aut']
        #TO=Topic.objects.get(topic_name=topic)
        WO=Webpage.objects.get(name=nam)
        AO=AccessRecord.objects.get_or_create(name=WO,date=dat,author=aut)[0]
        AO.save()

        return HttpResponse('<center><h1>Insertion of AccessRecord is Done</h1></center>') 
    return render(request,'insert_accessrecord.html',wd)   


def retrieve_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        MSTS=request.POST.getlist('topic')

        RWOS=Webpage.objects.none()
        for i in MSTS:
            RWOS=RWOS|Webpage.objects.filter(topic_name=i)

        d1={'RWOS':RWOS}
        return render(request,'display_webpage.html',d1)
    
    return render(request,'retrieve_webpage.html',d)


def retrieve_accessrecord(request):
    LWO=Webpage.objects.all()
    s={'LWO':LWO}

    if request.method=='POST':
        WOS=request.POST.getlist('nam')

        RARO=AccessRecord.objects.none()
        for j in WOS:
            RARO=RARO|AccessRecord.objects.filter(id=j)
        
        s1={'RARO':RARO}
        return render(request,'display_accessrecord.html',s1)
    return render(request,'retrieve_accessrecord.html',s)

def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'checkbox.html',d)