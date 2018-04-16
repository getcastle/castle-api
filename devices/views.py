from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from . import serializers
from devices.models import Device

from .mqtt import client

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

@api_view(['PUT'])
def update_device_feature(req, pk):
  # connect client to mosquitto broker
  client.connect('bridge.get-castle.com')

  # grab feature and val
  payload = req.data
  print(payload)

  for attr, val in payload.items():
    client.publish('cmnd/devices/{}/{}'.format(pk, attr), val)

  return Response(payload)