from rest_framework import routers
from .viewsets import BookViewSet

bookRoute = routers.DefaultRouter()

bookRoute.register(r'books', BookViewSet, basename='Books')