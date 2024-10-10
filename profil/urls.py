# profil/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ProfilViewSet

router = DefaultRouter()
router.register(r'profils', ProfilViewSet)

urlpatterns = [
    path('profils/', views.profil_list, name='profil_list'),
    path('profils/create/', views.profil_create, name='profil_form'),
    path('api/', include(router.urls)),# API yo'llarini router orqali qo'shamiz
]
