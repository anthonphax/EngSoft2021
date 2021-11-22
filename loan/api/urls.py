from rest_framework import routers
from .viewsets import *

loansRoutes = routers.DefaultRouter()

loansRoutes.register(r'loans', GetAllLoansViewSet, basename='loans')
loansRoutes.register(r'user/loan', LoanByUserViewSet, basename='loans')
