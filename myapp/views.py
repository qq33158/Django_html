from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random
from myapp.models import student

# Create your views here.
def base(request):
    return render(request,"base.html",locals())

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

# student example
def listone(request): 
	try: 
		unit = student.objects.get(cName="金城武") #讀取一筆資料
	except:
  		errormessage = " (讀取錯誤!)"
	return render(request, "listone.html", locals())

def listall(request):  
	students = student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
	return render(request, "listall.html", locals())
	
def insert(request):  #新增資料
    if request.method == 'POST':
        cName = request.POST['name']
        cSex =  request.POST['sex']
        cBirthday =  request.POST['birthday']
        cEmail = request.POST['email']
        cPhone =  request.POST['phone']
        cAddr =  request.POST['addr']
        unit = student.objects.create(cName=cName, cSex=cSex, cBirthday=cBirthday, cEmail=cEmail,cPhone=cPhone, cAddr=cAddr) 
        unit.save()  #寫入資料庫
        students = student.objects.all().order_by('-id')  #依id遞減排序
        return render(request, "listall.html", locals())
    else:
        return render(request,"insert.html",locals())
	
def modify(request):  #修改資料
    name = request.GET['name']
    unit = student.objects.get(cName=name)
    if request.method == 'POST':
        unit.cName = request.POST['name']
        unit.cSex = request.POST['sex']
        birthday = request.POST['birthday']
        birthday = ((birthday.replace('年','-')).replace('月','-')).replace('日','')
        unit.cBirthday = birthday
        unit.cEmail = request.POST['email']
        unit.cPhone = request.POST['phone']
        unit.cAddr = request.POST['addr']
        unit.save()  #寫入資料庫
        students = student.objects.all().order_by('-id')  #依id遞減排序
        return render(request, "listall.html", locals())
    else:
        sex = unit.cSex
        birthday = unit.cBirthday
        email = unit.cEmail
        phone = unit.cPhone
        addr = unit.cAddr
        return render(request,"modify.html",locals())

def delete(request,id=None):  #刪除資料
    name = request.GET['name']
    unit = student.objects.get(cName=name)
    unit.delete()
    students = student.objects.all().order_by('-id')
    return render(request, "listall.html", locals())

def listall2(request):  
	students = student.objects.all().order_by('id')  #依id遞增排序
	return render(request, "listall2.html", locals())