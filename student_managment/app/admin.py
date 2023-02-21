from django.contrib import admin
from app.models import student_dashboard,Student

# Register your models here.
@admin.register((Student))
class Stud(admin.ModelAdmin):
    list_display = ['id','Name','Email','Password']

@admin.register((student_dashboard))
class dashboard(admin.ModelAdmin):
    list_display = ['id','Course_Name','Fess','Duration','Description']