from django.db.models import Q
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )

from posts.api.permissions import IsOwnerOrReadOnly
from posts.api.pagination import PostLimitOffsetPagination, PostPageNumberPagination

User = get_user_model()


from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer,
    )


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST

# from django.shortcuts import render

# import json

# from rest_framework import generics
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny

# from django.contrib.auth import login, authenticate

# from .serializers import AccountSerializer
# from .models import Account


# class AuthRegister(APIView):
#     """
#     Register a new user.
#     """
#     serializer_class = AccountSerializer
#     permission_classes = (AllowAny,)

#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class AuthLogin(APIView):
#     ''' Manual implementation of login method '''
#     def post(self, request, format=None):
#         data = request.data
#         email = data.get('email', None)
#         password = data.get('password', None)

#         account = authenticate(email=email, password=password)
#         # Generate token and add it to the response object
#         if account is not None:
#             login(request, account)
#             return Response({
#                 'status': 'Successful',
#                 'message': 'You have successfully been logged into your account.'
#             }, status=status.HTTP_200_OK)

#         return Response({
#             'status': 'Unauthorized',
#             'message': 'Username/password combination invalid.'
#         }, status=status.HTTP_401_UNAUTHORIZED)