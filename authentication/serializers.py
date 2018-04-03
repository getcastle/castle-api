from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework import serializers

from .models import Profile

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')

class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(label='Email Address')
    email2 = serializers.EmailField(label='Confirm Email')

    class Meta:
        model = User
        fields = ('email', 'email2', 'password')
        extra_kwargs = {"password": {"write_only": True}}
        
    def validate(self, data):
        return data

    def validate_email(self, value):
        data = self.get_initial()
        email1 = data.get("email2")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match.")
        
        user_qs = User.objects.filter(email=email2)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")

        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get("email")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match.")
        return value

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(email = email)
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = ('id', 'user')

class UserLoginSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'profile')

# from django.contrib.auth import update_session_auth_hash

# from rest_framework import serializers

# from .models import Account

# class AccountSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True)
#     confirm_password = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = Account
#         fields = (
#             'id', 'email', 'username', 'date_created', 'date_modified',
#             'firstname', 'lastname', 'password', 'confirm_password')
#         read_only_fields = ('date_created', 'date_modified')

#     def create(self, validated_data):
#         return Account.objects.create_user(**validated_data)

#     def update(self, instance, validated_data):
#         instance.email = validated_data.get('email', instance.email)
#         instance.username = validated_data.get('username',
#                                                instance.username)
#         instance.firstname = validated_data.get('firstname',
#                                                 instance.firstname)
#         instance.lastname = validated_data.get('lastname',
#                                                instance.lastname)

#         password = validated_data.get('password', None)
#         confirm_password = validated_data.get('confirm_password', None)

#         if password and password == confirm_password:
#             instance.set_password(password)

#         instance.save()
#         return instance

#     def validate(self, data):
#         '''
#         Ensure the passwords are the same
#         '''
#         if data['password']:
#             print ("Here")
#             if data['password'] != data['confirm_password']:
#                 raise serializers.ValidationError(
#                     "The passwords have to be the same"
#                 )
#         return data
