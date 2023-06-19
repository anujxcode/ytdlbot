from email import message
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from pytube import YouTube
import os
# from django.contrib.messages import messages 

# Create your views here.
def index(request):
    return render(request,'index.html')


def download(request):
    if request.method == 'POST':
        if request.POST.get('yt_link') =='':
            return redirect("/")
        else:
            # youtube link
            global yt_link
            yt_link = request.POST.get('yt_link')

            # youtube get data
            ytvideo = YouTube(yt_link)
            title =  ytvideo.title
            yt_img = ytvideo.thumbnail_url
            duration = ytvideo.length
            views = ytvideo.views
            pubDate = ytvideo.publish_date
            video = ytvideo.streams.filter(progressive= True)

            audio = ytvideo.streams.filter(only_audio=True)
            # filter resolution by loop
            # res =[]
            # for i in video:
            #     res.append(i.resolution)

            # vidList = list(enumerate(video))
            # video.downlaod()
            context = {
                "duration":duration,
                'views':views,
                "title":title,
                "ytImg":yt_img,
                "vidList":video,
                "pubDate":pubDate,
                "audio":audio,
            }
            return render(request,'download.html',context)

    else:
        return render(request,'download.html')


def download_done(request, resolution):
    global yt_link
    homedir = os.path.expanduser("~")
    vddirs = homedir + '/Downloads/ytDownlaod/video'
    addirs = homedir + '/Downloads/ytDownload/audio'
    resx = resolution
    
    if request.method =='POST':
        ytobj = YouTube(yt_link).streams.filter(progressive= True, resolution= resx)
        ytobj.first().download(vddirs)


    elif request.method =='GET':
        ytaudio = YouTube(yt_link).streams.filter(only_audio=True, abr= resx)
        ytaudio.first().download(addirs)
    else:
        print("error")
    return render(request,'done.html')





def help(request):
    return render(request,'help.html')

def support(request):
    return render(request,'support.html')

