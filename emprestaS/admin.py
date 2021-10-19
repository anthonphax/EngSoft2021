from django.contrib import admin
from .users.models import Student

# Register your models here.
class Students(admin.ModelAdmin):
    list_display = ('id', 'user', 'cpf', 'gender', 'phoneNumber', 'address1', 'address2', 'cep', 'city')
    list_display_links = ('id', 'user')
    search_fields = ('user',)
    list_per_page = 20

admin.site.register(Student, Students)