from rest_framework import serializers
from  .models import User

class UserProfileCreateSerializer(serializers.ModelSerializer):
    password_repeat = serializers.CharField(write_only=True)
    class Meta:
        model = User
        
        fields = ['username', 'email', 'password', 'password_repeat']

    def validate(self, data):
        if data['password'] != data['password_repeat']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password_repeat')
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user