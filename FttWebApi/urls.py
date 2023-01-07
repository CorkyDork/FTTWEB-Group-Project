from django.contrib import admin
from django.urls import path
from FttWebApi import views

urlpatterns = [
    path('get-client-transactions/', views.ApiIsGetClientTransactions, name = "ApiIsGetClientTransactions"),
]