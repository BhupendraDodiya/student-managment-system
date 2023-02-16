from django.shortcuts import render

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