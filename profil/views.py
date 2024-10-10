from django.shortcuts import render, redirect
from rest_framework import viewsets

from .models import Profil
from .forms import ProfilForm
from .serializer import ProfilSerializer

# Django klassik views

def profil_list(request):
    profils = Profil.objects.all()
    return render(request, 'profil/profil_list.html', {'profils': profils})

def profil_create(request):
    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profil_list')
    else:
        form = ProfilForm()
    return render(request, 'profil/profil_form.html', {'form': form})

class ProfilViewSet(viewsets.ModelViewSet):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer

