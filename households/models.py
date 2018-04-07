from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

from django.utils import timezone

class Household(models.Model):
  """
  Represents a household
  """
  name = models.CharField(max_length=200)
  lastUpdated = models.DateTimeField(auto_now=True)
  createdAt = models.DateTimeField(default=timezone.now)

  members = models.ManyToManyField(
    User,
    through="HouseholdMember",
    through_fields=('household', 'user')
  )

  def __str__(self):
    """Return admin-friendly name of Household"""
    return self.name

class HouseholdMember(models.Model):
  """
  Through/relationship table mapping a user to a household since many users can be related to many housheolds and vice versa
  """
  user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
  household = models.ForeignKey(Household, related_name="household", on_delete=models.CASCADE)

  # access control
  owner = models.BooleanField(default=False)
  admin = models.BooleanField(default=False)

  # TBD:
  # invited to household
  # invitedAt = models.DateTimeField(null=True, blank=True)
  # invitedBy = models.ForeignKey(User, blank=True)
  # acceptedInvitationAt = models.DateTimeField(null=True, blank=True)

  # left household
  # leftAt = models.DateTimeField(null=True, blank=True)

  # kicked out of household
  # kickedAt = models.DateTimeField(null=True, blank=True)
  # kickedBy = models.ForeignKey(User, null=True, blank=True)
