"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from products.views import *
from users.views import *
from rest_framework import routers
from django.conf.urls import url

router = routers.DefaultRouter()
router.register('items', ItemViewSet, basename="Itens")
router.register('books', BookViewSet, basename="Book")
router.register('digital-medias', DigitalMediaViewSet, basename="DigitalMedia")
router.register('academic-works', AcademicWorkViewSet, basename="AcademicWork")
router.register('modelos', ModeloViewSet, basename="Model")
router.register('peripherals', PeripheralViewSet, basename="Peripheral")

router.register('student', StudentsViewSet, basename="Student")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]
