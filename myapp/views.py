from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random

# Create your views here.

def sayhello(request):
    return HttpResponse("Hello Django!")

def hello2(request,username):
    return HttpResponse("Hello"+username)

def hello3(request,username):
    now = datetime.now()
    return render(request,"hello3.html",locals())

def hello4(request,username):
    now = datetime.now()
    return render(request,"hello4.html",locals())

def dice(request):
    no1 = random.randint(1,6)
    no2 = random.randint(1,6)
    no3 = random.randint(1,6)
    return render(request,"dice.html",locals())

def show(request):
    person1 = {"name":"Ame","phone":"02-123456","age":"23"}
    person2 = {"name":"Gura","phone":"03-123456","age":"22"}
    person3 = {"name":"Ina","phone":"04-123456","age":"26"}
    persons = [person1,person2,person3]
    return render(request,"show.html",locals())

def djget(requset):
    name = requset.GET['name']
    city = requset.GET['city']
    return render(requset,"djget.html",locals())

def djpost(requset):
    if requset.method == 'POST':
        username = requset.POST['username']
        password = requset.POST['password']
        if username == 'ame' and password == '1234':
            return HttpResponse('歡迎光臨本站!')
        else:
            return HttpResponse('帳號密碼錯誤!')
    else:       
        return render(requset,"djpost.html",locals())