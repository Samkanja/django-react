from core.user.models import User
from core.user.serializers import UserSerializer
from rest_framework import serializers

class RegisterSerializer(UserSerializer):
    """Registration serializer for requests and user creation"""

    # Making sure the password is at least 8 characters long and no longer than 128 and can't be read
    # by the user

    password = serializers.CharField(max_length=128, min_length=8, write_only=True,required=True)

    class Meta:
        model = User

        fields = ['id','bio','avatar','email','username','first_name','last_name','password']


    def create(self, validated_data):
        # User the create_user method we wrote earlier for the Usermanager to create a new user

        return User.objects.create_user(**validated_data)