from django import template
from blog.models import *
from blog.utils import menu, b_menu

register = template.Library()


@register.simple_tag()
def get_menu():
    return menu


@register.simple_tag()
def get_b_menu():
    return b_menu


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('blog/tags/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
        return {"cats": cats, "cat_selected": cat_selected}
