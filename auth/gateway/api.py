from .models import Lead, UserProfile, UserMetaData, Role
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer, UserProfileSerializer, UserMetaDataSerializer, RoleSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer

class UserProfileSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserProfileSerializer

class UserMetaDataSet(viewsets.ModelViewSet):
    queryset = UserMetaData.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserMetaDataSerializer

class RoleSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoleSerializer