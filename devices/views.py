from rest_framework import generics, permissions
from . import serializers
from devices.models import Device


class HouseholdDeviceList(generics.ListAPIView):
  """
  Lists the devices from a particular household.
  """
  serializer_class = serializers.DeviceListSerializer
  permission_classes = (permissions.IsAuthenticated,)

  def get_queryset(self):
    """
    Returns a scoped queryset of the households a user belongs to.
    """
    # get the id of the desired household
    householdId = self.kwargs.get('householdId')
    return Device.objects.all().filter(household=householdId)
  
class HouseholdDeviceDetail(generics.RetrieveAPIView):
  """
  Lists the devices from a particular household.
  """
  queryset = Device.objects.all()
  serializer_class = serializers.DeviceSerializer
  permission_classes = (permissions.IsAuthenticated,)
