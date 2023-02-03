from django.db import models
from django_countries.fields import CountryField

from core.abstract_models import AbstractDefaultModels
from core.enums.fan_dealership_enums import Currency, StatusofAccessories
from core.validators import check_popularity


# Create your models here.
class Accessories(AbstractDefaultModels):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    year_seasons = models.IntegerField()
    price = models.IntegerField(default=10000)
    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.USD
    )

    cat = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
    )

    status = models.CharField(
        max_length=255,
        choices=StatusofAccessories.choices,
        default=StatusofAccessories.Available
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'Аксессуар'
        verbose_name_plural = 'Аксессуары'

    def __str__(self):
        return self.title

class Category(AbstractDefaultModels):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Popularity(AbstractDefaultModels):
    value = models.IntegerField(validators=[check_popularity], default=1)
    accessor = models.ForeignKey(
        Accessories,
        on_delete=models.PROTECT,
        related_name='popularity'
    )

    class Meta:
        ordering = ['value']
        verbose_name = 'Популярность'
        verbose_name_plural = 'Популярности'


class Fan_dealership(AbstractDefaultModels):
    name = models.CharField(max_length=255)
    specification = models.TextField(blank=True)
    location = CountryField(default='Germany')
    contact = models.EmailField()
    accessor = models.ForeignKey(
        Accessories,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Фаншоп'
        verbose_name_plural = 'Фаншопы'

    def __str__(self):
        return self.name
