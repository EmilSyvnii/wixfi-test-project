from rest_framework import serializers
from api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


a = {
    "first_name": "Andy",
    "last_name": "Robertson",
    "email": "andy@ffff",
    "password": "passw"
}