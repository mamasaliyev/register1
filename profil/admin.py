from django.contrib import admin
from .models import Profil

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'avatar')
    search_fields = ('username', 'email')


