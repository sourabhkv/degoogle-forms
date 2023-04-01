from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import csv
# Create your views here.
def signuppage(request):
    if request.method=='POST':
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")
        print(uname,email,pass1,pass2)
        if pass1==pass2:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login/')
        else:
            return HttpResponse("wrong passwd")


    return render(request,'signup.html')

@login_required(login_url='login')
def homepage(request):
    if request.method=='POST':
        recieved_data =dict(request.POST)
        with open('data.csv', mode='a') as file:
            writer = csv.writer(file)
            writer.writerow(
                (recieved_data["csrfmiddlewaretoken"][0],request.user.username,recieved_data['name'][0],recieved_data['usn'][0],recieved_data['email'][0],
                 recieved_data['semester'][0],recieved_data['branch'][0],recieved_data["Rating"][0],recieved_data["subject"][0],*recieved_data['programming-language'])
            )
        return HttpResponse('Form submitted succesfully')
    print(request.user.username)
    return render(request,'deform.html')

def loginpage(request):
    if request.method=="POST":
        uname = request.POST.get('username')
        passwd = request.POST.get('pass')
        print(uname,passwd)
        user = authenticate(request,username = uname,password = passwd)
        if user!=None:
            login(request,user)
            return redirect('home')
        else:
            HttpResponse("username or password is incorrect")
    return render(request,'login.html')

def logoutx(request):
    logout(request)
    return redirect('login')