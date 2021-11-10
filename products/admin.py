from django.contrib import admin
from .models import *

class Items(admin.ModelAdmin):
    list_display = ('id', 'itemName', 'created', 'updated', 'description', 'status')
    list_display_links = ('id', 'itemName', 'created', 'updated', 'description', 'status')
    search_fields = ('itemName',)
    list_per_page = 25

admin.site.register(Item, Items)
