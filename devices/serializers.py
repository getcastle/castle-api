from rest_framework import serializers

from authentication.serializers import UserSerializer
from.import models


class NetworkingAttributesSerializer(serializers.ModelSerializer):

  class Meta:
    model = models.DeviceNetworkAttributes
    exclude = ('device',)

class AttributePlugSerializer(serializers.ModelSerializer):

  class Meta:
    model = models.DeviceAttributes_Plug
    exclude = ('id',)

class AttributeSocketSerializer(serializers.ModelSerializer):

  class Meta:
    model = models.DeviceAttributes_Socket
    exclude = ('id',)

class AttributeSerializer(serializers.RelatedField):
  """
  Custom serializer that takes the source Device and returns the right attribute serializer depending on Device.deviceType
  """

  def to_representation(self, value):
    """
    Serialize bookmark instances using a bookmark serializer,
    and note instances using a note serializer.
    """
    if isinstance(value, models.DeviceAttributes_Plug):
      serializer = AttributePlugSerializer(value)
    elif isinstance(value, models.DeviceAttributes_Socket):
      serializer = AttributeSocketSerializer(value)
    else:
      raise Exception('Cannot serialize unexpected device type attributes')

    return serializer.data

class DeviceListSerializer(serializers.ModelSerializer):

    class Meta:
      model = models.Device
      exclude = ('household',)

class DeviceSerializer(serializers.ModelSerializer):
  # how to load from a different table given a
  # SEE: generic relations (http://www.django-rest-framework.org/api-guide/relations/#custom-relational-fields)
  claimedBy = UserSerializer()
  attributes = AttributeSerializer(read_only=True)
  networking = NetworkingAttributesSerializer()

  class Meta:
    model = models.Device
    exclude = ('household', 'attributesType', 'attributesId')
    # depth = 2
