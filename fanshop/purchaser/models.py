from django.db import models
from django_countries.fields import CountryField


from core.abstract_models import AbstractDefaultModels
from core.enums.purchaser_enums import SexofPurchaser
from core.validators import check_phonenum


# Create your models here.
class Purchaser(AbstractDefaultModels):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    sex = models.CharField(
        max_length=6,
        choices=SexofPurchaser.choices,
        default=SexofPurchaser.Female
    )
    location = CountryField(default='Germany')
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(
        max_length=13,
        validators=[check_phonenum]
    )


    class Meta:
        ordering = ['first_name']
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return self.first_name

class Balance(AbstractDefaultModels):
    value = models.DecimalField(max_digits=5, decimal_places=2)
    purch = models.ForeignKey(
        Purchaser,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['value']
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'

    def __str__(self):
        return self.purch
