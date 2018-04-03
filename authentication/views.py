from django.db.models import Q
from django.contrib.auth import get_user_model, authenticate
User = get_user_model()

from rest_framework import decorators

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

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

from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)

from . import serializers

# from posts.api.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner of this object.'
    # my_safe_method = ['GET', 'PUT']
    # def has_permission(self, request, view):
    #     if request.method in self.my_safe_method:
    #         return True
    #     return False

    def has_object_permission(self, request, view, obj):
        #member = Membership.objects.get(user=request.user)
        #member.is_active
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user

# from posts.api.pagination import PostLimitOffsetPagination, PostPageNumberPagination

class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10

class PostPageNumberPagination(PageNumberPagination):
    page_size = 20

class UserCreateAPIView(CreateAPIView):
    serializer_class = serializers.UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

# class UserLogin(APIView):
#     """
#     View to log users into the API
#     """
#     serializer_class = serializers.UserLoginSerializer
#     # permission_classes = [AllowAny]
    
#     # Logs a user in
#     def post(self, request):
#         """
#         Logs a user in to the server
#         """
#         data = request.data
#         serializer = serializers.UserLoginSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             print(serializer.data)
#             new_data = serializer.data
#             return Response(new_data, status=HTTP_200_OK)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@decorators.api_view(['POST'])
@decorators.permission_classes([AllowAny])
def register(req):
    """
    Registers a user with the application.

    @param      Request     req             RF's Request object

    @post       str         req.email       email of user logging in
    @post       str         req.password    password of user logging in
    @returns    Response
    """
    raise NotImplementedError

@decorators.api_view(['POST'])
@decorators.permission_classes([AllowAny])
def login(req):
    """
    Logs a user in to the server.

    @param      Request     req             RF's Request object

    @post       str         req.email       email of user logging in
    @post       str         req.password    password of user logging in
    @returns    Response
    """
    # TODO: validate for req.data.email
    email = req.data.get("email")
    password = req.data.get("password")

    # fetch user if user w email existts and verify pw
    user = authenticate(username=email, password=password)
    
    if user is not None:
        resp = {}

        # serialize user object
        serializer = serializers.UserLoginSerializer(user)
        resp["user"] = dict.copy(serializer.data)

        # generato token
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        resp["token"] = token
        return Response(resp)

    return Response({
        "error": {
            "code": "AUTH/INCORRECT_EMAIL_PASSWORD_COMBINATION",
            "message": "That email and password combination was incorrect."
        }
    }, status=HTTP_400_BAD_REQUEST)
