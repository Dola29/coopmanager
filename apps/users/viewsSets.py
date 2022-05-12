from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND

from . import models
from apps.users import serializers

class UserViewSet(ViewSet):
    """Crear y actualizar ususarios"""
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def list(self, request):
        data = models.User.objects.all()
        serializer = serializers.UserSerializer(data, many=True)
        return Response(serializer.data)
        
    def create(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

    def update(self, request, pk):
        try:
            user = models.User.objects.get(id=pk)
        except models.User.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

        serializer = serializers.UserSerializer(user, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Mensaje": "Registro Actualizado"}, status = HTTP_200_OK)

    def destroy(self, request, pk):
        try:
            user = models.User.objects.get(id=pk)
        except models.User.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

        user.delete()
        return Response("Registro Eliminado!")

class RoleViewSet(ModelViewSet):
    serializer_class = serializers.RoleSerializer
    queryset = models.Role.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
