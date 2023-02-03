from django.db import models

class Value(models.TextChoices):
    EUR = 'EUR', 'EUR'
    USD = 'USD', 'USD'
    RUB = 'RUB', 'RUB'