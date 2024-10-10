from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'phone', 'avatar', 'birth_date', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data.get('phone', None),
            avatar=validated_data.get('avatar', 'avatars/default-user-avatar.jpg'),
            birth_date=validated_data.get('birth_date', None)
        )
        user.set_password(validated_data['password'])  # Parolni xesh qilish
        user.save()
        return user
