from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('FttWebApp.urls')),
    path('auth/', include('UserAuthorization.urls')),
]