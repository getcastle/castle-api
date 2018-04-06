from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework import serializers

from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = ('id', 'user')

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    # input-only
    firstName = serializers.CharField(write_only=True)
    lastName = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'profile', 'password', 'firstName', 'lastName')
        extra_kwargs = {
            "password": {'write_only': True}
        }
    
    def validate_email(self, email):
        # check to see if it is a valid email str

        # check to see email is not being used
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise serializers.ValidationError("This email is already being used by another user.")

        return email
    
    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']

        # important - use both username and email (until username field is removed)
        user = User.objects.create(email=email, username=email)
        user.set_password(password)

        user.profile.firstName = validated_data.get('firstName', "")
        user.profile.lastName = validated_data.get('lastName', "")
        user.save()
        return user
