from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings
from django.utils.timezone import now


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a new user"""
        if not email:
            raise ValueError('Users must have an email')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """"Custom user model that supports user email"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'


class Patient(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    mobile = models.CharField(max_length=10, unique=True)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=3)

    def __str__(self):
        return self.fname


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=now)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
