from django.urls import path

from . import views

urlpatterns = [
  path('households', views.HouseholdList.as_view(), name='households.list'),
  path('household/<int:pk>', views.HouseholdDetail.as_view(), name='household.detail'),
  path('household/<int:pk>/devices', views.HouseholdDetail.as_view(), name='household.devices'),
]
