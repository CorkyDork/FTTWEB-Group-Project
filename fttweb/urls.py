from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('', include('FttWebApp.urls')),
    path('userauth/', include('UserAuthorization.urls')),
    path('api/', include('FttWebApi.urls')),
]