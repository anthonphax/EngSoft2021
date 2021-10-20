from rest_framework import routers
from emprestas.users.views import *
from emprestas.items.views import *

router = routers.DefaultRouter()

router.register('students', StudentsViewSet, basename='Students')
router.register('books', BooksViewSet, basename='Books')
router.register('digital-media', DigitalMediasViewSet, basename='DigitalMedias')
router.register('academic-work', AcademicWorksViewSet, basename='AcademicWorks')
router.register('modelo', ModelosViewSet, basename='Modelos')
router.register('device', DevicesViewSet, basename='Devices')
router.register('peripheral', PeripheralsViewSet, basename='Peripherals')