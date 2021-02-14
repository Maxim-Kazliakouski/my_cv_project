from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me, name='info_about_me'),
    path('about_me/', views.about_me, name='info_about_me'),
    path('personal_info/', views.person_page, name='per_info'),
    path('work_expirience/', views.work, name='work'),
    path('education/', views.edu, name='edu'),
    path('languages/', views.lang, name='lang'),
    path('skills/', views.skills, name='skills'),
    path('certificates/', views.cert, name='cert'),
    path('hobbies/', views.hob, name='hobbies'),
    path('personal_info_skype/', views.per_inf_skype, name='per_skype'),
    path('personal_info_phone', views.per_inf_phone, name='per_phone'),
    ]