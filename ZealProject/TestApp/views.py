from django.shortcuts import render,redirect
from django.http import HttpResponse
from TestApp.models import About_us,Contact,Course


# Create your views here.
def index(request):
    courses = Course.objects.all()
    return render(request,'TestApp/index.html',{'courses':courses})


def contactc(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        cn=Contact(name=name, email=email, message=message)
        cn.save()
    return render(request,'TestApp/index.html')

def about_us(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone_no=request.POST.get('phone_no')
        ab=About_us(name=name,email=email,phone_no=phone_no)
        ab.save()
    return render(request,'TestApp/index.html')

def course_view(request):
    courses = Course.objects.all()
    return render(request, 'TestApp/index.html',{'courses':courses})
