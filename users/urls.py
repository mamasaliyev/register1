from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserAPIViewSet

router = DefaultRouter()
router.register(r'users', UserAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
