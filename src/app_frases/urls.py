"""
URL configuration for app_frases project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

# URLS API
from rest_framework import routers
from app_api.views import FraseViewSet, AutorViewSet

# URLS Media
from django.conf import settings
from django.conf.urls.static import static

router = routers.SimpleRouter()
router.register(r'api_frases', FraseViewSet)
router.register(r'api_autores', AutorViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('autores.urls', namespace='autores')),
    path('biblioteca/', include('app_biblioteca.urls', namespace='app_biblioteca')),
    # path('api/', include('app_api.urls', namespace='app_api')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls