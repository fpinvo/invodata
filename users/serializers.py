from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model"""

    class Meta:
        model = User
        extra_kwargs = {
            'password': {'write_only': True}
        }
        fields = [
            'id',
            'first_name',
            'last_name',
            'company_name',
            'email',
            'username',
            'phone_number',
            'country',
            'password',
        ]
