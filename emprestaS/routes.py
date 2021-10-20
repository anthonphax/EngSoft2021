from rest_framework import routers
from emprestas.users.views import *
from emprestas.items.views import *

userRouter = routers.DefaultRouter()
itemRouter = routers.DefaultRouter()

userRouter.register('students', StudentsViewSet, basename='Students')

itemRouter.register('books', BooksViewSet, basename='Books')
itemRouter.register('digital-media', DigitalMediasViewSet, basename='DigitalMedias')
itemRouter.register('academic-work', AcademicWorksViewSet, basename='AcademicWorks')
itemRouter.register('modelo', ModelosViewSet, basename='Modelos')
itemRouter.register('device', DevicesViewSet, basename='Devices')
itemRouter.register('peripheral', PeripheralsViewSet, basename='Peripherals')