from rest_framework import serializers

from .models import Household

class HouseholdSerializer(serializers.ModelSerializer):
    
    class Meta:
      model = Household
      exclude = ('members',)