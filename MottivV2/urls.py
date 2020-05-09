"""MottivV2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework.authtoken import views
from rest_framework import routers
from apiPersonas.views import Login, Logout
from apiProductos.views import ProductoList

router = routers.DefaultRouter()
router.register(r'productos', ProductoList)


urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^api-auth/', include('rest_framework.urls')),
    path('apipersonas/1.0/', include(('apiPersonas.urls', 'apiPersonas'))),
    #path('apiproductos/1.0/', ProductoList.as_view(), name='producto_list'),
    path('api_generate_token/', views.obtain_auth_token),# Me permite responder con un token para el usuario correspondiente
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    url(r'^', include(router.urls))
]
