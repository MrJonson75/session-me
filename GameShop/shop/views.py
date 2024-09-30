from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *
from .utils import *

info = {}


class PostList(DataMixin, ListView):
    model = GamePost
    template_name = 'shop/post.html'
    context_object_name = 'page'
    # paginate_by = 3

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Блог Все категории')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return GamePost.objects.filter(is_published=True).select_related('cat')  # жадная загрузка связанных данных избегаем дубли запросов


class GameCategory(DataMixin, ListView):
    model = GamePost
    template_name = 'shop/post.html'
    context_object_name = 'page'
    allow_empty = False  # Вызывает исключение если страница не найдена

    def get_queryset(self):
        return GamePost.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related(
            'cat')  # жадная загрузка связанных данных

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      cat_selected=c.pk)
        # c_def = self.get_user_context(title='Категория - ' + str(context['page'][0].cat),
        #                               cat_selected=context['page'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


# def show_category(request, cat_slug):
#     cat = Category.objects.get(slug=cat_slug)
#     page_obj = GamePost.objects.filter(cat_id=cat.id)
#
#     if len(page_obj) == 0:
#         raise Http404()
#
#     context = {
#         'page_obj': page_obj,
#         'menu': menu,
#         'cat_selected': cat_slug,
#         'title': 'Блог',
#     }
#     return render(request, 'shop/post.html', context=context)


class ShowPost(DataMixin, DetailView):
    model = GamePost
    template_name = 'shop/post_open.html'
    slug_url_kwarg = 'post_slug'
    # pk_url_kwarg = 'post_pk'
    context_object_name = 'page'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['page'])
        return dict(list(context.items()) + list(c_def.items()))


# def show_post(request, post_slug):
#     post = get_object_or_404(GamePost, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 'shop/post_open.html', context=context)


class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'shop/post_add.html'
    success_url = reverse_lazy('blog')
    login_url = '/admin/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))


# def add_post(request):
#     '''Обработка формы добавить пост в блоге'''
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('blog')
#     else:
#         form = AddPostForm()
#     return render(request, 'shop/post_add.html',
#                   {
#                       'form': form,
#                       'menu': menu,
#                       'title': 'Добавление статьи',
#                   })


def games_platform(request):
    context = {
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'shop/platform.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте'
    }
    return render(request, 'shop/about.html', context=context)


def games(request):
    return HttpResponse('Магазин игр')


def cart(request):
    return HttpResponse('У Вас нет товаров')


def logoutuser(request):
    logout(request)
    return redirect('login')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'shop/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'shop/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
