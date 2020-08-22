from rest_framework import serializers
from .models import userProfile

class userProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = userProfile
        fields='__all__'

    def validate_email(self, value):
        if User.all_objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError('User with this email already exists.')

        return value.lower()

    def create(self, validated_data):
        password = validated_data.pop('password')
        email = validated_data.pop('email')
        user = User.objects.create(
            username=email.lower(),
            email=email.lower(),
            role_id=1,
            **validated_data)
        user.set_password(password)

        user.save()

        return user