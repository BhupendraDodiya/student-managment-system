from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

#dashboard
    path('dashboard/',views.dashboard), 

#sign in urls
    path('',views.index),
    path('sign_in_reg/',views.sign_in_reg),

#sign up urls
    path('sign-up/',views.sign_up),
    path('sign_up_reg/',views.sign_up_reg),
    

#courses urls
    path('courses/',views.courses),
    path('courses_add/',views.courses_add),
    path('delete/<int:uid>/',views.delete),
    path('update/<int:uid>/',views.update),
    path('upd/',views.upd),


#teachers url
    path('teachers/',views.teachers),
    path('addteacher/',views.addteacher),
    path('deleteteacher/<int:uid>/',views.deleteteacher.as_view()),
    path('updateteacher/<int:uid>/',views.updateteacher.as_view()),
    path('updteacher/',views.updteacher.as_view()),

#students url
    path('student/',views.student.as_view()),
    path('addstudent/',views.addstudent),
    path('deletestudent/<int:uid>/',views.deletestudent.as_view()),
    path('updatestudent/<int:uid>/',views.updatestudent),
    path('updstudent/',views.updstudent.as_view()),

   



]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
