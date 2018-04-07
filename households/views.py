from rest_framework import generics, permissions

from . import serializers
from .models import Household

class HouseholdList(generics.ListAPIView):
  """
  Allows a user to list and create the households they belong to.
  """
  serializer_class = serializers.HouseholdSerializer
  permission_classes = (permissions.IsAuthenticated,)

  def get_queryset(self, * args, ** kwargs):
    """
    Returns a scoped queryset of the households a user belongs to.
    """
    return self.request.user.household_set.all()

class HouseholdDetail(generics.RetrieveAPIView):
  """
  Allows a user to view and update a household they belong to.
  """
  queryset = Household.objects.all()
  serializer_class = serializers.HouseholdSerializer
  permission_classes = (permissions.IsAuthenticated,)