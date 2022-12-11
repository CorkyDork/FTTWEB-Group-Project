from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.pageHome, name = "pageHome"),
    path('contact', views.pageContactUs, name = "pageContactUs"),
    path('about', views.pageAboutUs, name = "pageAboutUs"),
    path('brokerdetails', views.pageBrokerDetails, name = "pageBrokerDetails"),
    path('fttpredict', views.pageftpPredict, name = "pageftpPredict"),
    path('reports', views.pageReport, name = "pageReport"),
    path('viewclients', views.pageViewClients, name = "pageViewClients"),
]