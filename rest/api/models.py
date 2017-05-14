from django.db import models

from filer.fields.file import FilerFileField


class Prueba(models.Model):
    file = FilerFileField(
        null=False
    )
    date = models.DateField(auto_now=True)


class Nested(models.Model):
    prueba = models.ForeignKey(Prueba, null=False)
    name = models.CharField(max_length=200, default='asd')
