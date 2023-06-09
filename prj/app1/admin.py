from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Item, ItemAdmin)