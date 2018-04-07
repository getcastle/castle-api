from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()
from .models import Household, HouseholdMember

from authentication.serializers import UserSerializer

class HouseholdListSerializer(serializers.ModelSerializer):
    
    class Meta:
      model = Household
      exclude = ('members',)
  
class HouseholdDetailSerializer(serializers.ModelSerializer):
  members = UserSerializer(many=True)

  class Meta:
    model = Household
    fields = '__all__'
