

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    try:
         name=request.COOKIES['Name']
         return render(request,'app/home.html',{'data':name})
    except:
        return render(request,'app/home.html')
        

def about(request):
    name=request.COOKIES['Name']
    #return render(request,'app/about.html')
    return render(request,'app/about.html',{'data':name})


def contact(request):
    name=request.COOKIES['Name']
    #return render(request,'app/contact.html')
    return render(request,'app/contact.html',{'data':name})

    
def service(request):
    #name=request.COOKIES['Name']
    return render(request,'app/service.html')
    #return render(request,'app/service.html',{'data':name})


def register(request):
    #name=request.COOKIES['Name']
    return render(request,'app/register.html')
    #return render(request,'app/.html',{'data':name})



def savedata(request):
    name=request.POST['name']
    email=request.POST['email']
    contact=request.POST['contact']
    city=request.POST['city']
    password=request.POST['password']
    # print(name)
    # print(email)
    # print(contact)
    # print(city)
    # print(password)
    response=render(request,'app/login.html')
    response.set_cookie('Name',name)
    response.set_cookie('Email',email)
    response.set_cookie('Contact',contact)
    response.set_cookie('City',city)
    response.set_cookie('Password',password)
    return response
    

def login(request):
    #name=request.COOKIES['Name']
    return render(request,'app/login.html')



def logindata(request):
    EmailId=request.POST['email']
    Password=request.POST['password']
    
    email_id=request.COOKIES['Email']
    pwd=request.COOKIES['Password']
    #print(EmailId)
    #print(Password)
    
    if EmailId==email_id and Password==pwd:
        name=request.COOKIES['Name']
        #print(name)
        return render(request,'app/home.html',{'data':name})
    
    
    
def logout(req):
    data=render(req,'app/home.html')
    data.delete_cookie('name')
    data.delete_cookie('email')
    data.delete_cookie('contact')
    data.delete_cookie('city')
    data.delete_cookie('password')
    return data
    
    
    
    
    
    
    