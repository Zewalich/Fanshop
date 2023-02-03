# Generated by Django 4.1.4 on 2023-01-22 19:44

import core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('year_seasons', models.IntegerField()),
                ('price', models.IntegerField(default=10000)),
                ('currency', models.CharField(choices=[('EUR', 'EUR'), ('USD', 'USD'), ('RUB', 'RUB')], default='USD', max_length=3)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Out_of_stock', 'Out_of_stock')], default='Available', max_length=255)),
            ],
            options={
                'verbose_name': 'Аксессуар',
                'verbose_name_plural': 'Аксессуары',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Popularity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=1, validators=[core.validators.check_popularity])),
                ('accessor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='popularity', to='fan_dealership.accessories')),
            ],
            options={
                'verbose_name': 'Популярность',
                'verbose_name_plural': 'Популярности',
                'ordering': ['value'],
            },
        ),
        migrations.CreateModel(
            name='Fan_dealership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('specification', models.TextField(blank=True)),
                ('contact', models.EmailField(max_length=254)),
                ('accessor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fan_dealership.accessories')),
            ],
            options={
                'verbose_name': 'Фаншоп',
                'verbose_name_plural': 'Фаншопы',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='accessories',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fan_dealership.category'),
        ),
    ]