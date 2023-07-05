from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics

from .models import Producto, Categoria, OrdendeCompra, Profile
from django.contrib.auth.models import User, Group

from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, UpdateAPIView, ListAPIView, \
    RetrieveUpdateDestroyAPIView, DestroyAPIView
from .serializers import ProductoSerializer, CategoriaSerializer, OrdendeCompraSerializer, UserSerializer, \
    ProductoSearchSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


class UserListView(ListView):
    model = User  # Especifica el modelo a utilizar (User en este caso)
    template_name = 'user_list.html'  # Especifica el nombre de la plantilla para mostrar la lista de usuarios
    context_object_name = 'object_list'  # Especifica el nombre de la variable de contexto para la lista de usuarios
    paginate_by = 10  # Especifica el número de usuarios por página
    queryset = User.objects.all()  # Especifica la consulta para obtener la lista de usuarios
    ordering = ['username']  # Especifica el ordenamiento de la lista de usuarios


@permission_classes((AllowAny,))
class productoListApi(ListAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all().order_by('id')
#   queryset = Producto.objects.filter(id_categoria=1).order_by('id')


@permission_classes((AllowAny,))
class productoListMacBoxAPI(ListAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.filter(id_categoria=1).order_by('id')


@permission_classes((AllowAny,))
class productoListMonitoresAPI(ListAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.filter(id_categoria=2).order_by('id')


@permission_classes((AllowAny,))
class productoListPerifericosAPI(ListAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.filter(id_categoria=3).order_by('id')


@permission_classes((AllowAny,))
class productoListRedesAPI(ListAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.filter(id_categoria=4).order_by('id')


@permission_classes((AllowAny,))
class productoListOfertasdelMesAPI(ListAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.filter(id_categoria=5).order_by('id')


@permission_classes((AllowAny,))
class productoListPortatilesAPI(ListAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.filter(id_categoria=6).order_by('id')


@permission_classes((AllowAny,))
class categoriaListApi(ListAPIView):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all().order_by('id')


@permission_classes((AllowAny,))
class OrdendeCompraAPI(PermissionRequiredMixin, CreateAPIView):
    queryset = OrdendeCompra.objects.all()
    serializer_class = OrdendeCompraSerializer
    permission_required = 'shop.add_ordendecompra'


@permission_classes((AllowAny,))
class categoriaListApi(ListAPIView):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all().order_by('id')


# Class para crear un producto usando CreateAPIView
class ProductoCreateAPI(PermissionRequiredMixin, CreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_required = 'shop.add_producto'


# Class para mostrar los datos de un producto en especifico usando RetrieveAPIView
@permission_classes((AllowAny,))
class ProductDetailView(RetrieveAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


# Class para API de busqueda de productos por nombreProducto
@permission_classes((AllowAny,))
class ProductoSearchAPIView(generics.ListAPIView):
    serializer_class = ProductoSearchSerializer

    def get_queryset(self):
        query = self.request.GET.get('q', '')  # Obtener el parámetro de búsqueda de la solicitud GET
        queryset = Producto.objects.filter(nombreProducto__icontains=query)  # Realizar la búsqueda en el atributo nombreProducto
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)  # Serializar los resultados
        return Response(serializer.data)


# Class para actualizar datos de usuario y profile en la misma API

class UserSerializer(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
