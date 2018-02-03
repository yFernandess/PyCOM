# coding: utf-8

from django.db import models

class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    value = models.DecimalField('Valor', max_digits=6, decimal_places=2)
    bar_code = models.CharField(u'Código de Barras', max_length=13, unique=True)

    def __unicode__(self):
        return "{} - {}: {} R$".format(self.bar_code, self.name, self.value)