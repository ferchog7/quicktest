from django.http import Http404
from rest_framework import status
from rest_framework.response import Response


from quicktest.mixins import MixinAuth
from .models import Bill, BillProduct
from .serializers import BillSerializer, BillProductSerializer


class BillList(MixinAuth):
    """
    List all bills, or create a new bill.
    """
    def get(self, request, format=None):
        bills = Bill.objects.all()
        serializer = BillSerializer(bills, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BillDetail(MixinAuth): 
    """
    Retrieve, update or delete a bill instance.
    """
    def get_object(self, pk):
        try:
            return Bill.objects.get(pk=pk)
        except Bill.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bill = self.get_object(pk)
        serializer = BillSerializer(bill)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bill = self.get_object(pk)
        serializer = BillSerializer(bill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BillProductList(MixinAuth):
    """
    List all bills, or create a new bill.
    """
    def get(self, request, pk, format=None):
        billproducts = BillProduct.objects.filter(bill_id=pk)
        serializer = BillProductSerializer(billproducts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BillProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)