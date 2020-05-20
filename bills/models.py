from django.db import models
from products.models import Product
from clients.models import Client

# Create your models here.
class Bill(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=250, verbose_name='Nombre')
    nit = models.IntegerField(verbose_name='NIT')
    code = models.IntegerField(verbose_name='Código')

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'


class BillProduct(models.Model):
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)