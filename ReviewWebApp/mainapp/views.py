from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
# Create your views here.
from .models import Review


def home(request):
    return render(request,'main614261.html')
def login(request):
    if request.method=="POST":
        username=request.POST['uname']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('Reviews')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
def register(request):
    if request.method=='POST':
        first_name=request.POST['Firstname']
        last_name=request.POST['Lastname']
        email=request.POST['E-mail']
        username=first_name+last_name
        password1=request.POST['fpassword']
        password2=request.POST['spassword']
        if password1==password2:
            user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
            user.save()
            return redirect('login')
        else:
            return HttpResponse("Passwords mismatch")
    else:
        return render(request,'register.html')
def Reviews(request):
    if request.method=="POST":
        name=request.POST['Name']
        pname = request.POST['Product']
        review = request.POST['Review']
        rating = request.POST['Rating']
        recommend = request.POST['Recommend']
        review=Review(Name=name,Product_name=pname,Review=review,Rating=rating,Recommendation=recommend)
        review.save()
        return render(request,'Review.html',{'Message':"Added Successfully...Thank You for sharing your feedback !"})
    else:
        return render(request,'Review.html')
def fetch(request):
    data=Review.objects.all()
    return render(request,"a.html",{'rev':data})
def logout(request):
    auth.logout(request)
    return redirect('/')
def contact(request):
    return render(request,'Contact.html')
def about(request):
    return render(request,'about.html')
