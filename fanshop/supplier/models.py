from django.db import models

from django_countries.fields import CountryField

from core.abstract_models import AbstractDefaultModels

from core.enums.supplier_enums import Value


# Create your models here.
class Supplier(AbstractDefaultModels):
    name = models.CharField(max_length=255)
    location = CountryField(default='Germany')
    contact = models.EmailField()
    attribute = models.CharField(max_length=255)
    info = models.TextField(blank=True)
    founding_date = models.DateField(null=True, blank=True)
    found = models.ForeignKey(
        'Founder',
        on_delete=models.PROTECT,
    )

    fanshops = models.ManyToManyField(
        'fan_dealership.Fan_dealership',
        related_name='supplier_fanshops'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name

class Founder(AbstractDefaultModels):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    age = models.IntegerField()
    company = models.CharField(max_length=255)
    fortune = models.DecimalField(max_digits=9, decimal_places=2)
    value = models.CharField(
        max_length=3,
        choices=Value.choices,
        default=Value.USD
    )

    class Meta:
        ordering = ['first_name']
        verbose_name = 'Основатель'
        verbose_name_plural = 'Основатели'

    def __str__(self):
        return self.first_name