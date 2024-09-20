from django.db import models


# Create your models here.

class Buyer(models.Model):
    """Модель описания Пользователя"""
    name = models.CharField(max_length=30,
                            db_index=True,
                            verbose_name='Username')        # имя покупателя (username аккаунта)
    balance = models.DecimalField(max_digits=12,
                                  decimal_places=2,
                                  verbose_name='Balance')   # баланс(DecimalField)
    age = models.IntegerField(max_length=3,
                              verbose_name='Age')           # возраст.

    def __str__(self):
        return self.name


class Game(models.Model):
    """Модель описания продукта"""
    title = models.CharField(max_length=250, db_index=True,
                             verbose_name='Game title')               # - название игры
    slug = models.SlugField(max_length=200, db_index=True)
    cost = models.DecimalField(max_digits=15, decimal_places=2,
                               verbose_name='Price')                  # - цена(DecimalField)
    size = models.DecimalField(max_digits=20, decimal_places=2,
                               verbose_name='File size')              # - размер файлов игры(DecimalField)
    description = models.TextField(blank=True,
                                   verbose_name='Description')        # - описание(неограниченное кол - во текста)
    age_limited = models.BooleanField(default=False)                  # - ограничение возраста 18 +
                                                                      # (BooleanField, по умолчанию False)
    buyer = models.ManyToManyField(Buyer, related_name='buyer')         # - покупатель обладающий игрой
                                                                        # (ManyToManyField).У каждого покупателя
                                                                        # может быть игра и у каждой игры может
                                                                        # быть несколько обладателей.

    def __str__(self):
        return self.title
