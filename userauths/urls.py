from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from userauths import views

urlpatterns = [
    path('register/', views.registration, name="register"),
    path('signup/', views.signup, name="signup"),
]