from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_judo_student/', views.add_judo_student, name='add_judo_student'),
    path('add_karate_student/', views.add_karate_student, name='add_karate_student'),
    path('add_aikido_student/', views.add_aikido_student, name='add_aikido_student'),
    path('add_kendo_student/', views.add_kendo_student, name='add_kendo_student'),
    path('add_jujitsu_student/', views.add_jujitsu_student, name='add_jujitsu_student'),
    path('search/', views.search, name='search'),
]

