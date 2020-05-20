from django.db import models

# Create your models here.
class Client(models.Model):
    document = models.IntegerField(verbose_name='Documento de identidad')
    first_name = models.CharField(max_length=200, verbose_name='Nombres')
    last_name = models.CharField(max_length=200, verbose_name='Apellidos')
    email = models.EmailField(verbose_name='Correo electrónico')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'