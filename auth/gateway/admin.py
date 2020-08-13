from django.contrib import admin
from gateway.models import UserProfile, Role, UserMetaData
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Role)
admin.site.register(UserMetaData)