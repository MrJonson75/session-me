from django.contrib import admin
from .models import *

# admin.site.register(GamePost)
admin.site.register(UserExtension)


@admin.register(GamePost)
class GamePostAdmin(admin.ModelAdmin):
    '''
    Изменение в Админ панели отображения полей базы GamePost
    '''
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published',)
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content',)
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''
    Изменение в Админ панели отображения полей базы Category
    '''
    prepopulated_fields = {'slug': ('name',)}
