from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import AuthSerializer


class AuthView(viewsets.ModelViewSet):
    serializer_class = AuthSerializer
    queryset = User.objects.all()
