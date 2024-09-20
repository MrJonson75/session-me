# Generated by Django 5.1.1 on 2024-09-20 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30, verbose_name='Username')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Balance')),
                ('age', models.IntegerField(max_length=3, verbose_name='Age')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=250, verbose_name='Game title')),
                ('slug', models.SlugField(max_length=200)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Price')),
                ('size', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='File size')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('age_limited', models.BooleanField(default=False)),
                ('buyer', models.ManyToManyField(related_name='buyer', to='task1.buyer')),
            ],
        ),
    ]
