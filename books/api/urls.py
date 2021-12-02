from rest_framework import routers
from .viewsets import *

bookRoute = routers.DefaultRouter()

bookRoute.register(r'items', BookViewSet, basename='Books')
bookRoute.register(r'items/loan', LoanBookViewSet, basename='LoanBook')