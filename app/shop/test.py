from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
import requests

url = 'http://127.0.0.1:3010/shop/UserAndProfileUpdate/'
token = 'f00ad59e61061fb232d4d1d56fa44fcff9a6ec98'

data = {
    "username": "usuario01",
    "email": "usuario01@gmail.com",
    "first_name": "Pepito",
    "last_name": "Perez",
    "profile": {
        "telephone_number": "56484894",
        "address": "Av. Siempre Viva 123",
    }
}

response = requests.patch(url, headers={'Authorization': f'Token {token}'}, json=data)

if response.status_code == 200:
    # La solicitud se realizó correctamente
    print('Los datos se actualizaron correctamente')

    # Consultar la base de datos para verificar que los datos se han actualizado correctamente
    user = User.objects.get(username='usuario01')
    print(f'Nombre: {user.first_name} {user.last_name}')
    print(f'Correo electrónico: {user.email}')
    print(f'Teléfono: {user.profile.telephone_number}')
    print(f'Dirección: {user.profile.address}')
else:
    # La solicitud no se realizó correctamente
    print(f'Error al actualizar los datos: {response.status_code} - {response.text}')