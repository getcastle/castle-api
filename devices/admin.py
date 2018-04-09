from django.contrib import admin

from . import models

# class KitAdmin(admin.ModelAdmin):
#   pass

class DeviceAdmin(admin.ModelAdmin):
  search_fields = ('household__name',)
  list_display = ('deviceType', 'isOnline', 'isOn', 'household', 'name' )

class DeviceAttributesAdmin(admin.ModelAdmin):
  pass

# admin.site.register(models.Kit, KitAdmin)
admin.site.register(models.Device, DeviceAdmin)
admin.site.register(models.DeviceAttributes_Plug, DeviceAttributesAdmin)
admin.site.register(models.DeviceAttributes_Socket, DeviceAttributesAdmin)
