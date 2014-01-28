# -*- coding: utf-8 -*-
from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Банк')
    URL = models.URLField(max_length = 300, blank = True)
    xpath = models.CharField(max_length = 300, blank = True)

    def __unicode__(self):
        pass
class BankContacts(models.Model):
    contact_type = (
        ('ad', u'Адрес'),
        ('tl', u'Телефон'),
        ('ml', u'Электронная почта'),
    )
    bank = models.ForeignKey(Bank)
    contact = models.CharField(max_length=2, choices=contact_type, verbose_name=u'Вид информации')
    value = models.CharField(max_length = 200, verbose_name = u'Значение')

class BankRates(models.Model):
    rate_type = (
        ('USD', u'Американский доллар'),
        ('UER', u'Евро'),
        ('UAH', u'Украинская гривна'),
        ('GBP', u'Британский фунт'),
    )

    bank = models.ForeignKey(Bank)
    rate = models.CharField(max_length = 3, choices=rate_type, verbose_name=u'Валюта')
    value = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name=u'Курс')
    checktime = models.DateTimeField(auto_now_add = True, verbose_name=u'Время обновления')