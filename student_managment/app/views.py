from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from app.models import Student
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def courses(request):
    return render(request,'courses.html')

def dashboard(request):
    return render(request,'dashboard.html')

def employees(request):
    return render(request,'employees.html')

def notifications(request):
    return render(request,'notifications.html')

def pg_dashboard(request):
    return render(request,'pg_dashboard.html')

def profile(request):
    return render(request,'profile.html')

def sign_up(request):
    return render(request,'sign-up.html')

def tables(request):
    return render(request,'tables.html')

def tenants(request):
    return render(request,'tenants.html')

def viewstudents(request):
    return render(request,'viewstudents.html')

#create action views

def sign_up_reg(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        if Student.objects.filter(Email=email).exists():
            return render (request,'sign-up.html',{'msg':'Email Already Exist'})
        else:
            Student.objects.create(Name=name,Email=email,Password=password)
            return redirect('/')

def sign_in_reg(request):
    if request.method =="POST":
        email = request.POST['email']
        password = request.POST['password']
        if Student.objects.filter(Email=email).exists():
            inst = Student.objects.get(Email=email)
            psw = inst.Password
            if check_password(password,psw):
                return redirect('/dashboard/')
            else:
                messages.error(request,'Password Incorrect')
                return redirect('/')
        else:
            messages.error(request,'Email not Exist')
            return redirect('/')
        
