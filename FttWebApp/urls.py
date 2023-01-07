from django.contrib import admin
from django.urls import path
from FttWebApp import views



urlpatterns = [
    path('', views.viewIsHome, name = "viewIsHome"),
    path('contact/', views.viewIsContactUs, name = "viewIsContactUs"),
    path('mydetails/', views.viewIsMyDetails, name = "viewIsMyDetails"),
    path('fttpredict/', views.viewIsPredictions, name = "viewIsPredictions"),
    path('myreports/', views.viewIsReports, name = "viewIsReports"),
    path('myclients/', views.viewIsMyClients, name = "viewIsMyClients"),
]