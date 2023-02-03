from django.core.exceptions import ValidationError

def check_popularity(value):
    if value > 5 or value < 1:
        raise ValidationError('Популярность определяется значением от 1 до 5')

def check_phonenum(phonenum):
    if len(phonenum) != 13 or phonenum[0] != '+':
        raise ValidationError('Проверьте правильность введённого номера')