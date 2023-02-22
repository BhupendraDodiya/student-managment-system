from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from app.models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def courses(request):
    res = student_dashboard.objects.all()
    return render(request,'courses.html',{'tab':res})

def dashboard(request):
    res = student_dashboard.objects.all()
    return render(request,'dashboard.html',{'res':res})

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
    stud = Student.objects.all()
    return render(request,'viewstudents.html',{'stud':stud})

#create action views
def delete(request,uid):
    student_dashboard.objects.filter(id=uid).delete()
    return redirect('/courses/')


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
        
def courses_add(request):
    if request.method=='POST':
        cname = request.POST['cname']
        fess = request.POST['fess']
        duration = request.POST['duration']
        description = request.POST['description']
        if student_dashboard.objects.filter(Course_Name=cname).exists():
            return render(request,'courses.html',{'msg':'Course already exist'})
        else:
            student_dashboard.objects.create(Course_Name=cname,Fess=fess,Duration=duration,Description=description)
            return redirect('/courses/')

def update(request,uid):
    res = student_dashboard.objects.get(id=uid)
    return render(request,'upd.html',{'row':res})

def upd(request):
    if request.method=="POST":
        row = request.POST['row']
        cname = request.POST['coursename']
        fess = request.POST['fess']
        duration = request.POST['duration']
        description = request.POST['description']
        student_dashboard.objects.filter(id=row).update(Course_Name=cname,Fess=fess,Duration=duration,Description=description)
        return redirect('/courses/')

def addstudent(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        college = request.POST.get("college")
        degree = request.POST.get("degree")
        address = request.POST.get("address")
        course = request.POST.get("course")
        total_amount = request.POST.get("total_amount")
        paid_amount = request.POST.get("paid_amount")
        due_amount = request.POST.get("due_amount")
        stu_course = student_dashboard.objects.get(id=course)
        if AddStudents.objects.filter(email=email).exists():
            messages.error(request,'Email already exists')
            return redirect('/viewstudents/')

        elif AddStudents.objects.filter(mobile=mobile).exists():
            messages.error(request,'mobile number already exists')
            return redirect('/viewstudents/')

        else:
            AddStudents.objects.create(name=name,email=email,mobile=mobile,address=address,
            college=college,degree=degree,course=course,total_amount=total_amount,
            paid_amount=paid_amount,due_amount=due_amount)

            messages.success(request,'student added successfully')
            