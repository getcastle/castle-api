from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from rest_framework_jwt import views as jwt_views
from . import views

urlpatterns = [
    path('login', views.login, name='auth.login'),
    path('register', views.UserRegistrar.as_view(), name='auth.register'),
    path('token/verify', jwt_views.verify_jwt_token, name='auth.token.verify'),
    path('token/refresh', jwt_views.refresh_jwt_token, name='auth.token.refresh'),
]