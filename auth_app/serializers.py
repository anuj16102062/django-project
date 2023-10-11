from rest_framework import serializers
from .models import User

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_phone(self, value):
        # Cellular Number should be integer
        if not value.isdigit():
            raise serializers.ValidationError("Invalid Cellular number format")
        return value
