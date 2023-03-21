from django.contrib import admin
from app.models import Course,User,AddTeacher,Students

# Register your models here.
@admin.register((User))
class user(admin.ModelAdmin):
    list_display = ['id','Name','Email','Password']

@admin.register((Course))
class course(admin.ModelAdmin):
    list_display = ['id','Course_Name','Fess','Duration','Description',]

@admin.register((Students))
class student(admin.ModelAdmin):
    list_display = ['id','name','email','mobile','Picture','address','college','degree','total_amount','paid_amount','due_amount','course']

@admin.register((AddTeacher))
class teacher(admin.ModelAdmin):
    list_display = ['id','Name','Age','JoiningDate','Experience','Image','Email','Contact','Gender','Course']