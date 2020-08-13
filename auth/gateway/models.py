from django.db import models
from django.contrib.auth.models import User
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
    date_created    = models.DateTimeField()
    date_updated    = models.DateTimeField()
    date_deleted    = models.DateTimeField()

    def __str__(self):
        return self.user.name

class Role(models.Model):
    name            = models.CharField(max_length=255)
    description     = models.CharField(max_length=255)
    date_created    = models.DateTimeField()
    date_updated    = models.DateTimeField()
    date_deleted    = models.DateTimeField()


class UserMetaData(models.Model):
    user_id	        = models.OneToOneField(User, on_delete=models.CASCADE)
    last_login      = models.DateTimeField()
    user_status	    = models.CharField(max_length=255)
    register_date   = models.DateTimeField()
    token           = models.CharField(max_length=255)
