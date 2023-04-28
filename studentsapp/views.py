from django.shortcuts import render,redirect
from .models import StudentsData

def mainpage(request):
    students=StudentsData.objects.all()
    return render(request,'mainpage.html',{'students':students})

def add_student(request):
    if request.method=='GET':
        return render(request,'add_student.html')
    else:
        StudentsData(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        email=request.POST['email'],
        mobile=request.POST['mobile'],
        course=request.POST['course'],
        fee=request.POST['fee'],
        location=request.POST['location']
        ).save()
        return redirect('mainpage')
