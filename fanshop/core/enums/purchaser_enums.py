from django.db import models


class SexofPurchaser(models.TextChoices):
    Male = 'Male', 'Male'
    Female = 'Female', 'Female'