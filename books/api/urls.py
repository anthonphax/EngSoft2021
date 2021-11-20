from rest_framework import routers
from .viewsets import *

bookRoute = routers.DefaultRouter()

bookRoute.register(r'books', BookViewSet, basename='Books')
bookRoute.register(r'books/loan', LoanBookViewSet, basename='LoanBook')