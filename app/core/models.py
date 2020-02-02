from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

  def create_user(self, email, password=None, **extrafields):
    """Creates and saves a new user"""
    if not email:
      raise ValueError('Users must have as email address')
    user = self.model(email=self.normalize_email(email), **extrafields)
    user.set_password(password)
    user.save(using=self._db)

    return user


class User(AbstractBaseUser, PermissionsMixin):
  """Custom user model that supports using email instead of username"""
  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  objects = UserManager()

  USERNAME_FIELD = 'email'
