from django.contrib import admin
from .models import *

# admin.site.register(GamePost)



@admin.register(GamePost)
class GamePostAdmin(admin.ModelAdmin):
    '''
    Изменение в Админ панели отображения полей базы GamePost
    '''
    list_display = ('id', 'title', 'time_create', 'photo', 'status',)
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content',)
    list_editable = ('status',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''
    Изменение в Админ панели отображения полей базы Category
    '''
    list_display = ('id', 'name',)
    prepopulated_fields = {'slug': ('name',)}
