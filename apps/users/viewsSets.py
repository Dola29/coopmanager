from urllib import request
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from . import models
from apps.users import serializers

class UserViewSet(ModelViewSet):
    """Crear y actualizar ususarios"""
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')
    authentication_classes = (TokenAuthentication,)
