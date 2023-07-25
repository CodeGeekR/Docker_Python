from django.urls import path
from shop.views import UserListView
from django.urls import re_path
from .views import productoListApi, productoListMacBoxAPI, productoListMonitoresAPI, productoListPerifericosAPI, \
    productoListRedesAPI, productoListOfertasdelMesAPI, productoListPortatilesAPI, OrdendeCompraAPI, \
    ProductoCreateAPI, UserAndProfileUpdateView, ProductDetailView, ProductoSearchAPIView
from .views import categoriaListApi


urlpatterns = [
    path("listView/", UserListView.as_view(), name="listView"),
    path("", UserListView.as_view(), name="listView"),
]

app_name = 'shop'

urlpatterns = [
    re_path(r"^getproducts$", productoListApi.as_view(), name="getproducts"),
    re_path(r"^getproductsmacbox", productoListMacBoxAPI.as_view(), name="getproductsmacbox"),
    re_path(r"^getproductsmonitors", productoListMonitoresAPI.as_view(), name="getproductsmonitors"),
    re_path(r"^getproductsperifericos", productoListPerifericosAPI.as_view(), name="getproductsperifericos"),
    re_path(r"^getproductsredes", productoListRedesAPI.as_view(), name="getproductsredes"),
    re_path(r"^getproductsofertasdelmes", productoListOfertasdelMesAPI.as_view(), name="getproductsofertasdelmes"),
    re_path(r"^getproductsportatiles", productoListPortatilesAPI.as_view(), name="getproductsportatiles"),
    re_path(r"^getcategories", categoriaListApi.as_view(), name="getcategories"),
    re_path(r"^ordendecompra", OrdendeCompraAPI.as_view(), name="ordendecompra"),
    re_path(r"^createproducto", ProductoCreateAPI.as_view(), name="createproducto"),
    re_path(r'^productDetail/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='productDetail'),
    re_path(r'^productos_search/', ProductoSearchAPIView.as_view(), name='productos-search'),
    re_path(r'^UserAndProfileUpdate/', UserAndProfileUpdateView.as_view(), name='UserAndProfileUpdate'),
]
