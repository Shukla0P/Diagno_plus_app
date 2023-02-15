from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='HOME'),
    path('testcase',views.testcase1,name='furst'),
    path('contact',views.contacts,name='contacts'),
    path('links',views.links,name='links'),
    path('home',views.index),
    path('cirrhosis',views.cirrhosis),
    path('brain_tumor',views.tumor),
    path('heart_disease',views.hdisease),
    path('cirr',views.cirr),
    path('btumor',views.btumor),
    path('hdisease2',views.hdisease2),
]
