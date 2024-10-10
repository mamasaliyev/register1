# project/urls.py
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Users app yo'llari
    path('', include('users.urls')),  # Foydalanuvchi yo'llarini asosiy sahifadan boshlaymiz

    # Profil app yo'llari
    path('', include('profil.urls')),  # Profil yo'llarini asosiy sahifadan boshlaymiz

    # Foydalanuvchilar va profil uchun API marshrutlari
    path('api/', include('users.urls')),  # Users API
    path('api/', include('profil.urls')),  # Profil API
]

# Media fayllar uchun (faqat DEBUG rejimida)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
