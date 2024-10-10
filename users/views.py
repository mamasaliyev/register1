from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from .models import User
from .serializers import UserSerializer

class UserAPIViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'login']:
            self.permission_classes = [AllowAny]
        return super(UserAPIViewSet, self).get_permissions()

    def perform_create(self, serializer):
        serializer.save()

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'muvafffaqiyatli amalga oshirildi.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'malumot notogri.'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def logout(self, request):
        logout(request)
        return Response({'message': 'muvaffaqiyatli amalga oshirildi.'}, status=status.HTTP_200_OK)
