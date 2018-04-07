from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()
from .models import Household, HouseholdMember

class MemberSerializer(serializers.ModelSerializer):
  """
  """
  pass

class HouseholdSerializer(serializers.ModelSerializer):
    
    class Meta:
      model = Household
      exclude = ('members',)
