from django.db.models import *

from .models import *

menu = [
    {'title': "O сайте", 'url_name': "about"},
    {'title': "Домой", 'url_name': "home"},
    {'title': "Магазин", 'url_name': "games"},
    {'title': "Блог", 'url_name': "blog"},
    {'title': "Корзина", 'url_name': "cart"},
]

b_menu = [
    {'title': "Добавить Статью", 'url_name': "add_post"}
]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('name'))
        context['menu'] = menu
        context['cats'] = cats
        if self.request.user.is_authenticated:
            context['b_menu'] = b_menu
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)
