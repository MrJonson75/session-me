from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse
from .models import Buyer, Game

# Create your views here.

info = {}


def games_platform(request):
    return render(request, 'platform.html')


def games(request):
    Games = Game.objects.all()
    context = {
        "Games": Games,
    }
    return render(request, "games.html", context)


def cart(request):
    status_cart = "Извините, Ваша корзина пуста"
    return render(request, 'cart.html', {"status_cart": status_cart})


def sign_up(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            users = Buyer.objects.all()
            for user in users:
                if user.name == username:
                    info["error"] = 'Пользователь уже существует'
                    return render(request, 'registration_page.html', {'info': info})

            if password != repeat_password:
                info["error"] = 'Пароли не совпадают'
                return render(request, 'registration_page.html', {'info': info})
            else:
                Buyer.objects.create(name=username, password=password, age=age)
                info["error"] = f'Регистрация прошла успешно, Приветствуем, {username}!'
                return render(request, 'registration_page.html', {'info': info})


    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form})
