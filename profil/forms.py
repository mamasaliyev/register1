from django import forms
from .models import Profil

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['username', 'email', 'avatar']

