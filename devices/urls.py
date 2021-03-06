from django.urls import path

from . import views

urlpatterns = [
  path('household/<int:householdId>/devices', views.HouseholdDeviceList.as_view(), name='household.devices.list'),
  path('household/<int:householdId>/devices/<int:pk>', views.HouseholdDeviceDetail.as_view(), name='household.devices.detail'),
  path('devices/<int:pk>', views.update_device_feature, name='household.device.update'),
]
