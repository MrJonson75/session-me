from django.contrib import admin
from .models import *

# admin.site.register(Buyer)
# admin.site.register(Game)

# Register your models here.

@admin.register(Game)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size', 'age_limited',)
    fields = [('title', 'cost', 'size', 'age_limited'), 'description', 'buyer',]
    list_filter = ('title', 'age_limited', 'buyer',)
    search_fields = ('title',)


@admin.register(Buyer)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'balance',)
    fields = [('name', 'age', 'balance'), 'password']
    search_fields = ('name',)