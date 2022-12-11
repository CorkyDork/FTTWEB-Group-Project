from django.contrib import admin
from django.urls import path, include
from UserAuthorization import views

urlpatterns = [
    path('', views.pageSignIn, name = "pageSignIn"),
    path('post-signin/', views.postSignIn, name = "pagePostSignIn"),
    path('post-signup/', views.postSignUp, name = "pagePostSignUp"),
    path('post-password-reset/', views.postPasswordReset, name = "pagePostPasswordReset"),
    path('logout/', views.pageLogout, name="pageLogout"),
    path('post-firebase-social-signin/', views.postFirebaseSocialSignin, name="pagePostFirebaseSocialSignin"),
]