from django.contrib import admin

from . import models
# Register your models here.

class HouseholdAdmin(admin.ModelAdmin):
  """
  """
  search_fields = ('name',)

class HouseholdMemberAdmin(admin.ModelAdmin):
  """
  """
  search_fields = ('user__email',)
  list_display = ('household', 'user', 'owner', 'admin')
  list_select_related = ('household', 'user')

admin.site.register(models.Household, HouseholdAdmin)
admin.site.register(models.HouseholdMember, HouseholdMemberAdmin)
