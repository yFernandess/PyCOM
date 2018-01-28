from django.db import models

class Produto(models.Model):
    name = models.CharField('Nome', max_length=100)
    value = models.DecimalField('Valor', max_digits=6, decimal_places=2)
    bar_code = models.CharField('Código de Barras', max_length=13, unique=True)

    def to_dict(self):
        return {
            "name": self.name,
            "value": float(self.value),
            "bar_code": self.bar_code
        }

    def __str__(self):
        return "{} - {}: {} R$".format(self.bar_code, self.name, self.value)
