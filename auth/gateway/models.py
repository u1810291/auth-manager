from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Создайте свои модели здесь.

class UserProfile(models.Model):
    user            = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    f_name          = models.CharField(max_length=255)
    l_name          = models.CharField(max_length=255)
    m_name          = models.CharField(max_length=255)
    INN             = models.IntegerField()
    phone           = models.IntegerField()
    passport        = models.CharField(max_length=255)
    address         = models.CharField(max_length=255)
    email           = models.CharField(max_length=255)
    role_id         = models.IntegerField()
    date_created    = models.DateTimeField(auto_now_add=True)
    date_updated    = models.DateTimeField(auto_now_add=True)
    date_deleted    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name

class Role(models.Model):
    name            = models.CharField(max_length=255)
    description     = models.CharField(max_length=255)
    date_created    = models.DateTimeField(auto_now_add=True)
    date_updated    = models.DateTimeField(auto_now_add=True)
    date_deleted    = models.DateTimeField(auto_now_add=True)


class UserMetaData(models.Model):
    user_id	        = models.OneToOneField(User, on_delete=models.CASCADE)
    last_login      = models.DateTimeField(auto_now_add=True)
    user_status	    = models.CharField(max_length=255)
    register_date   = models.DateTimeField(auto_now_add=True)
    token           = models.CharField(max_length=255)


class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=255, blank=True)
    owner = models.ForeignKey(User, 
    related_name="leads", on_delete=models.CASCADE,
    null=True)
    created_at = models.DateTimeField(auto_now_add=True)
