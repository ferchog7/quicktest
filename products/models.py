from django.db import models

# Create your models here.
class Product(models.Model): 
    name = models.CharField(max_length=250, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    attribute = models.CharField(max_length=250, verbose_name='Atributo')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'