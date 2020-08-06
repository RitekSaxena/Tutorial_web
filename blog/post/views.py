from django.shortcuts import render,redirect
from .models import Chapters, Course,Videos,Content
# Create your views here.

def home(request):

    return render(request, 'post/home.html')

def landing(request):
    coursess = Course.objects.all

    return render(request, 'post/landing.html',{'courses':coursess})

def chapters(request, pk):

    courses = Course.objects.get(id = pk)
    chapter = reversed(Chapters.objects.filter(course=courses))

    

    return render(request, 'post/chapters.html', {'chapters':chapter, 'course':courses})
    

def learning(request, key):
    chapterss= Chapters.objects.get(id=key)

    vdos = reversed(Videos.objects.filter(chapter=chapterss))

    return render(request, 'post/learning.html', {'chapter':chapterss,'vdos':vdos})
    
def lecture(request, key):


    vdo1  = Videos.objects.get(id = key)
    content = Content.objects.get(chapter = vdo1)

    if vdo1.premium_status == False :
        return render(request, 'post/lecture.html',{'vdo':vdo1, 'content':content})
    else:
        return redirect('premium')
    
    
def premium(request):
    
    return render(request, 'post/premium.html')