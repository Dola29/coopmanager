from cgi import print_directory
from rest_framework import serializers
from .models import User, Role
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'description', 'created_at']
    
    def create(self, validated_data):
        return super().create(validated_data)

class RoleListSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id')
    label = serializers.CharField(source='name')
    class Meta:
        model = Role
        fields = ['value', 'label', 'description', 'created_at']

class UserListSerializer(serializers.ModelSerializer):
    
    role = RoleListSerializer()

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'role', 'created_at']
        extra_kwargs = {
            'password' : {'write_only': True}
        }
    depth = 1

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'role', 'created_at']
        extra_kwargs = {
            'password' : {'write_only': True}
        }

    depth = 1
    
    def create(self, validated_data):
        try:
            if 'role' not in validated_data:
                the_role = 4
            else:
                the_role = Role.objects.get(name = validated_data["role"])
            

        except Role.DoesNotExist:
            return Response({'message':'Rol no encontrado'},status=HTTP_404_NOT_FOUND)

        user = User.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
            role = the_role
        )
        user.save()
        return user

    def update(self, instance, validated_data):
        try:
            the_role = Role.objects.get(name = validated_data["role"])
        except Role.DoesNotExist:
            return Response({'message':'Rol no encontrado'},status=HTTP_404_NOT_FOUND)

        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        instance.email =  validated_data["email"]
        instance.name =  validated_data["name"]
        instance.role = the_role
        instance.set_password(password)
        

