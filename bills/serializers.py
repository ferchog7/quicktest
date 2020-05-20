from rest_framework import serializers
from .models import Bill, BillProduct

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['pk', 'client_id', 'company_name', 'nit', 'code']


class BillProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillProduct
        fields = ['pk', 'bill_id', 'product_id']