from django.conf.urls import url
from django.contrib import admin

from .views import (
    UserCreateAPIView,
    UserLoginAPIView
    )

urlpatterns = [
    url(r'^/login$', UserLoginAPIView.as_view(), name='login'),
    url(r'^/register$', UserCreateAPIView.as_view(), name='register'),
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






