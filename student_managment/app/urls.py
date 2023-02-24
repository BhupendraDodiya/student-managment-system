from django.urls import path
from app import views

urlpatterns = [
    path('',views.index),
    path('sign_in_reg/',views.sign_in_reg),
    path('courses/',views.courses),
    path('courses_add/',views.courses_add),
    path('dashboard/',views.dashboard),
    path('employees/',views.employees),
    path('notifications/',views.notifications),
    path('pg_dashboard/',views.pg_dashboard),
    path('profile/',views.profile),
    path('sign-up/',views.sign_up),
    path('sign_up_reg/',views.sign_up_reg),
    path('tables/',views.tables),
    path('viewstudents/',views.viewstudents),
    path('delete/<int:uid>',views.delete),
    path('update/<int:uid>',views.update),
    path('upd/',views.upd),
    path('addstudent/',views.addstudent),
    path('teachers/',views.teachers),
]
