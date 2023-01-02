from django.shortcuts import render
import csv
# Create your views here.

def adddata(request):
    if request.method=="POST":
        dict1=request.POST
        print(dict1)
        with open("data.csv","a") as csvfile:
            wrt=csv.writer(csvfile)
            wrt.writerow([dict1['Name'],dict1['email'],dict1['csrfmiddlewaretoken']])

    return render(request,"register.html")

def home(request):
    return render(request,"home.html")
