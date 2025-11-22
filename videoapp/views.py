from django.shortcuts import render,redirect
from .models import Video
from django.db.models import Q
from django.contrib import messages

def helloworld(request):
    all_videos = Video.objects.all()
    return render(request, 'index.html',{'videos':all_videos})

def video(request,pk):
    video = Video.objects.get(id=pk)
    return render(request, 'video.html',{'video':video})

def search(request):
    if request.method=='POST':
        searched = request.POST['searched']
        searched = Video.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
        if not searched:
            messages.success(request,("Not Found!!!!!!!!!!"))
            return redirect('home')
        else:
            return render(request,'search.html',{'searched':searched})
    return render(request,'search.html',{})
