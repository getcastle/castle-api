from django.db import models
from django.utils import timezone
from django.db.models import signals
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from households.models import Household

User = get_user_model()

# class ManufacturedDevice(models.Model):
#   """
#   Back office model representing a device that was just created.
#   """
#   pass

# class Kit(models.Model):
#   """
#   Represents a subscription kit of Devices.
#   """
#   pass

class Device(models.Model):
  """
  Logistical/identity information about a claimed device.
  """
  name = models.CharField(max_length=255)
  isOn = models.BooleanField(default=False)
  isOnline = models.BooleanField(default=False)

  # device type
  DEVICE_TYPES = (
    ('PLUG', 'Plug'),
    ('SOCKET', 'Socket'),
  )
  deviceType = models.CharField(max_length=255, choices=DEVICE_TYPES)

  # device attributes
  attributesType = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  attributesId = models.PositiveIntegerField(blank=True, null=True)
  attributes = GenericForeignKey('attributesType', 'attributesId')

  # kit
  # kit = models.ForeignKey(Kit, on_delete=models.PROTECT)
  # kitPaidFor = models.BooleanField(default=True)

  # households
  household = models.ForeignKey(Household, related_name='devices', on_delete=models.PROTECT)
  claimedAt = models.DateTimeField(default=timezone.now)
  claimedBy = models.ForeignKey(User, on_delete=models.PROTECT)

  def __str__(self):
    return str(self.id)

class DeviceNetworkAttributes(models.Model):
  """
  Real-time info about the networking attributes of a device.
  """
  device = models.OneToOneField(
      Device,
      on_delete=models.CASCADE,
      primary_key=True,
      related_name='networking'
  )
  isOnline = models.BooleanField(default=False)
  lastOnline = models.DateTimeField(blank=True, null=True)

class DeviceAttributes(models.Model):
  """
  Abstract class relating a set of device attributes to a Device.
  """
  # device = models.OneToOneField(
  #     Device,
  #     on_delete=models.CASCADE,
  #     primary_key=True,
  #     parent_link=True,
  #     related_name='attributes'
  # )
  device = GenericRelation(Device)

  class Meta:
    abstract = True

class DeviceAttributes_Plug(DeviceAttributes):
  """
  Device attributes for devices that are `Plug` devices.
  """
  isOn = models.BooleanField(default=False)
  lastOn = models.DateTimeField(blank=True, null=True)

class DeviceAttributes_Socket(DeviceAttributes):
  """
  Device attributes for devices that are `Socket` devices.
  """
  isOn = models.BooleanField(default=False)
  lastOn = models.DateTimeField(blank=True, null=True)
  brightness = models.PositiveSmallIntegerField(default=0) # range: 0 - 32,767

@receiver(signals.post_save, sender=Device)
def create_device_attributes(sender, instance, created, **kwargs):
  """
  Creates auxiliary feature records for a Device upon its creation.
  """
  if created:
    devType = instance.deviceType

    # create attributes
    attr = None
    if devType == 'PLUG': # PLUG
      attr = DeviceAttributes_Plug.objects.create()
    elif devType == 'SOCKET':
      attr = DeviceAttributes_Socket.objects.create()
    
    # create & relate networking attributes
    networking = DeviceNetworkAttributes.objects.create(device=instance)

    # assign attributes to device
    if attr:
      instance.attributes = attr
      instance.save()
