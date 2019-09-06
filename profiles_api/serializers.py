from rest_framework import serializers

from .models import UserProfile, ProfileFeedItem


class HelloSerializer(serializers.Serializer):
    """Serializes the name field for testing API"""
    name = serializers.CharField(max_length=15)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return new User"""
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user


class ProfileFeedSerializer(serializers.ModelSerializer):
    """Serializes profile feed objects"""

    class Meta:
        model = ProfileFeedItem
        fields = ('id', 'status_text', 'created_on', 'user_profile')
        extra_kwargs = {
            'user_profile': {
                'read_only': True
            }
        }
