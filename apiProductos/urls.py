from django.urls import path
from .views import ProductoList

urlpatterns = [
    path('producto/', ProductoList.as_view(), name='producto_list'),
]
