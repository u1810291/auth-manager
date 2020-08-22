from rest_framework import serializers
from .models import UserProfile, Lead, UserMetaData, Role


class UserProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = UserProfile
        fields='__all__'


        
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields='__all__'


        
class UserMetaDataSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = UserMetaData
        fields='__all__'


        
class LeadSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Lead
        fields='__all__'
