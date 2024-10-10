from rest_framework import serializers
from .models import Profil

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = ['id', 'username', 'email', 'avatar']
