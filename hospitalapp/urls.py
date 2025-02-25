
from django.contrib import admin
from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index , name='index'),
    path('starter/', views.starter , name='starter'),
    path('service/', views.service, name='service'),
]
