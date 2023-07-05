from .models import Profile, Categoria, SubCategoria, Producto, Descuento, OrdendeCompra, Ciudades, Departamentos
from django.contrib.auth.models import Group, User
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.serializers import (
    SerializerMethodField
)


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(ModelSerializer):
    id_categoria = CategoriaSerializer(many=True)

    class Meta:
        model = Producto
        fields = '__all__'


class OrdendeCompraSerializer(ModelSerializer):
    class Meta:
        model = OrdendeCompra
        fields = ['id_user', 'id_producto', 'cantidad', 'id_forma_pago', 'id_estado_compra']


# CODIGO PARA ASIGNAR UN GRUPO DE USUARIOS AUTOMATICAMENTE AL CREAR UN USUARIO USANDO DJ_REST_AUTH
class CustomRegisterSerializer(RegisterSerializer):
    def create(self, request):
        user = super().create(request)
        group, created = Group.objects.get_or_create(name='Clientes')
        user.groups.add(group)
        user.save()
        return user

    def custom_signup(self, request, user):
        group, created = Group.objects.get_or_create(name='Clientes')
        user.groups.add(group)
        print(">usuario creado exitosamente")
        user.save()


# Serializer para API de busquedas de productos por nombreProducto
class ProductoSearchSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombreProducto']


# CREAR SERIALIZER PARA UNA API UPDATEAPIVIEW DE DJ_REST_AUTH QUE PERMITA ACTUALIZAR LOS DATOS DE USER Y PROFILE EN LA MISMA API

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('imagenProfile', 'telephone_number', 'address', 'department', 'city')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        profile = instance.profile
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        profile.telephone_number = profile_data.get('telephone_number', profile.telephone_number)
        profile.address = profile_data.get('address', profile.address)
        profile.department = profile_data.get('department', profile.department)
        profile.city = profile_data.get('city', profile.city)
        instance.save()
        profile.save()
        return instance
