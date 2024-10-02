from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import *
from .models import *
from .utils import *

info = {}


class PostList(DataMixin, ListView):
    model = GamePost
    template_name = 'blog/post.html'
    context_object_name = 'page'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Блог Все категории')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return GamePost.objects.filter(status='published').select_related(
            'cat')  # жадная загрузка связанных данных избегаем дубли запросов


class GameCategory(DataMixin, ListView):
    model = GamePost
    template_name = 'blog/post.html'
    context_object_name = 'page'
    allow_empty = False  # Вызывает исключение если страница не найдена

    def get_queryset(self):
        return GamePost.objects.filter(cat__slug=self.kwargs['cat_slug'], status='published').select_related(
            'cat')  # жадная загрузка связанных данных

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


class ShowPost(DataMixin, DetailView):
    model = GamePost
    template_name = 'blog/post_open.html'
    slug_url_kwarg = 'post_slug'
    # pk_url_kwarg = 'post_pk'
    context_object_name = 'page'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['page'])
        return dict(list(context.items()) + list(c_def.items()))


class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'blog/post_add.html'
    success_url = reverse_lazy('blog')
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class UpdatePage(DataMixin, UpdateView):
    model = GamePost
    fields = ['title', 'content', 'photo', 'status', 'cat']
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('blog')
    title_page = 'Редактирование статьи'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Редактирование статьи')
        return dict(list(context.items()) + list(c_def.items()))


def games_platform(request):
    context = {
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'blog/platform.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте'
    }
    return render(request, 'blog/about.html', context=context)


def logoutuser(request):
    logout(request)
    return redirect('login')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'blog/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/register.html'
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
