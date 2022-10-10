"""Ebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# basic URL Configurations
from django.urls import include, path
# import routers
from rest_framework import routers

from core.views import Ebookviewset
  
# import everything from views
from core import views
  
# define the router
router = routers.DefaultRouter()
  
# define the router path and viewset to be used
router.register(r'ebook', Ebookviewset)
router.register(r'delete-post', views.DeletePostViewSet)  # NOQA


# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
