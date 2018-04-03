from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    firstName= models.CharField(max_length=200)
    lastName= models.CharField(max_length=200)
    phoneNumber= models.CharField(max_length=10)
    birthday= models.DateField(null=True, blank=True)
    createdAt= models.DateTimeField(auto_now_add=True)
    lastUpdated= models.DateTimeField(auto_now=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Creates and links additional Profile object on User object creation.
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Updates Profile object after User object is saved"
    """
    instance.profile.save()

# class AccountManager(BaseUserManager):
#     def create_user(self, email, password=None, **kwargs):
#         # Ensure that an email address is set
#         if not email:
#             raise ValueError('Users must have a valid e-mail address')

#         # Ensure that a username is set
#         if not kwargs.get('username'):
#             raise ValueError('Users must have a valid username')

#         account = self.model(
#             email=self.normalize_email(email),
#             username=kwargs.get('username'),
#             firstname=kwargs.get('firstname', None),
#             lastname=kwargs.get('lastname', None),
#         )

#         account.set_password(password)
#         account.save()

#         return account

#     def create_superuser(self, email, password=None, **kwargs):
#         account = self.create_user(email, password, kwargs)

#         account.is_admin = True
#         account.save()

#         return account


# class Account(AbstractBaseUser):
#     username = models.CharField(unique=True, max_length=50)
#     email = models.EmailField(unique=True)

#     firstname = models.CharField(max_length=100, blank=True)
#     lastname = models.CharField(max_length=100, blank=True)

#     date_created = models.DateTimeField(auto_now=True)
#     date_modified = models.DateTimeField(auto_now_add=True)

#     is_admin = models.BooleanField(default=False)

#     objects = AccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def get_full_name(self):
#         return ' '.join(self.firstname, self.last_login)
