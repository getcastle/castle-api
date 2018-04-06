from django.contrib.auth import get_user_model, authenticate
from rest_framework import permissions, decorators

from rest_framework_jwt.settings import api_settings
from rest_framework.generics import CreateAPIView

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST

from . import serializers

User = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class UserRegistrar(CreateAPIView):
    """
    Create (register) a new user.
    """
    queryset = User.objects.all()
    # serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, req, * args, ** kwargs):
        resp = {}
        # create user
        data = serializers.UserSerializer(data=req.data)

        # validate data
        data.is_valid(raise_exception=True)
        
        user = data.save()
        resp["user"] = dict.copy(data.data)
        
        # generate token
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        resp["token"] = token
        return Response(resp)

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.AllowAny])
def login(req):
    """
    Logs a user in.

    @param      Request     req             RF's Request object

    @post       str         req.email       email of user logging in
    @post       str         req.password    password of user logging in
    @returns    Response
    """
    # TODO: validate req.data.email, req.data.password
    email = req.data.get("email")
    password = req.data.get("password")

    # fetch user if user w email existts and verify pw
    user = authenticate(username=email, password=password)
    
    if user is not None:
        resp = {}

        # serialize user object
        serializer = serializers.UserSerializer(user)
        resp["user"] = dict.copy(serializer.data)

        # generate token
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
