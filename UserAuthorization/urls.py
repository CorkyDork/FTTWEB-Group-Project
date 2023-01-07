from django.contrib import admin
from django.urls import path
from UserAuthorization import views

urlpatterns = [
    path('api/post-signin/', views.ApiIsSignIn, name = "ApiIsSignIn"),
    path('api/post-signup/', views.ApiIsSignUp, name = "ApiIsSignUp"),
    path('api/post-password-reset/', views.ApiIsPasswordReset, name = "ApiIsPasswordReset"),
    path('api/logout/', views.ApiIsLogout, name="ApiIsLogout"),
    path('api/post-firebase-social-signin/', views.ApiIsFirebaseSocialSignin, name="ApiIsFirebaseSocialSignin"),
]