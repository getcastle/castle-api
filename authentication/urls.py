from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'/login', views.login, name='login'),
    url(r'/register', views.UserCreateAPIView.as_view(), name='register'),
]
# from django.conf.urls import include, url
# from .views import AuthLogin, AuthRegister
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

# urlpatterns = [
#     url(r'^login/', obtain_jwt_token),
#     url(r'^token-refresh/', refresh_jwt_token),
#     url(r'^token-verify/', verify_jwt_token),
#     url(r'^register/$', AuthRegister.as_view()),

#     # URL Created for manual login logic
#     # url(r'^login/$', AuthLogin.as_view()),
# ]






