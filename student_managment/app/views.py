from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.decorators import login_required
from app.models import *
from django.contrib import messages
from django.views import View

#dashboard view start

def dashboard(request):
    res = Course.objects.all()
    teacher = AddTeacher.objects.all()
    student = Students.objects.all()
    course_count= res.count()
    teacher_count= teacher.count()
    student_count= student.count()
    return render(request,'dashboard.html',{'res':res,'teacher':teacher,'student':student,
                                'course_count':course_count,'teacher_count':teacher_count,'student_count':student_count})

#dashboard view end

# sigin in views start
def index(request):
    return render(request,'index.html')

def sign_in_reg(request):
    if request.method =="POST":
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(Email=email).exists():
            inst = User.objects.get(Email=email)
            psw = inst.Password
            if check_password(password,psw):
                return redirect('/dashboard/')
            else:
                messages.error(request,'Password Incorrect')
                return redirect('/')
        else:
            messages.error(request,'Email not Exist')
            return redirect('/')
        
# sigin in views end

# sigin up views start

def sign_up(request):
    return render(request,'sign-up.html')

def sign_up_reg(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        if User.objects.filter(Email=email).exists():
            return render (request,'sign-up.html',{'msg':'* Email Already Exist'})
        else:
            User.objects.create(Name=name,Email=email,Password=password)
            return redirect('/')

# sign up views end


# courses  views start

def courses(request):
    res = Course.objects.all()
    return render(request,'courses.html',{'tab':res})

def courses_add(request):
    if request.method=='POST':
        cname = request.POST['cname']
        fess = request.POST['fess']
        duration = request.POST['duration']
        description = request.POST['description']
        if Course.objects.filter(Course_Name=cname).exists():
            messages.error(request,'Course already exist')
            return redirect('/courses/')
        else:
            Course.objects.create(Course_Name=cname,Fess=fess,Duration=duration,Description=description)
            res = Course.objects.all()
            return render(request,'courses.html',{'tab':res})

def update(request,uid):
    res = Course.objects.get(id=uid)
    return render(request,'course_update.html',{'row':res})

def upd(request):
    if request.method=="POST":
        row = request.POST['row']
        cname = request.POST['coursename']
        fess = request.POST['fess']
        duration = request.POST['duration']
        description = request.POST['description']
        Course.objects.filter(id=row).update(Course_Name=cname,Fess=fess,Duration=duration,Description=description)
        res = Course.objects.all()
        return render(request,'courses.html',{'tab':res})
    
def delete(request,uid):
    Course.objects.filter(id=uid).delete()
    return redirect('/courses/')

# courses views end


        
# teachers views start

def teachers(request):
    tab = Course.objects.all()
    data = AddTeacher.objects.all()
    return render(request,'teachers.html',{'data':data,'tab':tab})

def addteacher(request):
    if request.method =="POST":
        Name = request.POST['name']
        Age = request.POST['age']
        Joiningdate = request.POST['joiningdate']
        Experience = request.POST['experience']
        Image = request.FILES.get('image')
        Email = request.POST['email']
        Contact = request.POST['contact']
        Gender = request.POST['gender']
        course = request.POST['course']
        course = Course.objects.get(id=course)
        if AddTeacher.objects.filter(Contact=Contact).exists():
            messages.error(request,'teacher already exist')
            return redirect('/teachers/')
        else:
            AddTeacher.objects.create(Name=Name,Age=Age,JoiningDate=Joiningdate,Experience=Experience,
                                        Image=Image,Email=Email,Contact=Contact,Gender=Gender,Course=course)
            return redirect('/teachers/')
        
class deleteteacher(View):
    def get(self,request,uid):
        AddTeacher.objects.filter(id=uid).delete()
        return redirect('/teachers/')
    
class updateteacher(View):
    def get(self,request,uid):
        row = AddTeacher.objects.get(id=uid)
        return render(request,'teacher_update.html',{'row':row})
    
class updteacher(View):
    def post(self,request):
        id = request.POST['row']
        Name = request.POST['name']
        Age = request.POST['age']
        Experience = request.POST['experience']
        AddTeacher.objects.filter(id=id).update(Name=Name,Age=Age,Experience=Experience)
        return redirect('/teachers/')

# teachers views end
    
#Students view start

class student(View):
    def get(self,request):
        cou = Course.objects.all()
        student = Students.objects.all()
        return render(request,'viewstudents.html',{'cou':cou,'stud':student})
    
      
class deletestudent(View):
    def get(self,request,uid):
        Students.objects.filter(id=uid).delete()
        return redirect('/student/')
    
def updatestudent(request,uid):
    id = Students.objects.get(id=uid)
    return render(request,'student_update.html',{'id':id})

class updstudent(View):
    def post(self,request):
        id = request.POST['ro']
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        Students.objects.filter(id=id).update(name=name,email=email,address=address)
        return redirect('/student/')
    
def addstudent(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        Picture = request.FILES.get('image')
        address = request.POST['address']
        college = request.POST['college']
        degree = request.POST['degree']
        total_amount = request.POST['total_amount']
        paid_amount = request.POST['paid_amount']
        due_amount = request.POST['due_amount']
        course = request.POST['course']
        course = Course.objects.get(id=course)
        print(Picture)
        if Students.objects.filter(email=email).exists():
            messages.error(request,'student already exist')
            return redirect('/student/')
        else:
            Students.objects.create(name=name,email=email,mobile=mobile,Picture=Picture,address=address,
                                    college=college,degree=degree,total_amount=total_amount,paid_amount=paid_amount,
                                    due_amount=due_amount,course=course)
            return redirect('/student/')
    
#Students view end