from django.http import Http404, HttpResponse
from rest_framework import status
from rest_framework.response import Response

from quicktest.mixins import MixinAuth
from bills.models import Bill
from .models import Client
from .serializers import ClientSerializer
    

class ClientList(MixinAuth):
    """
    List all clients, or create a new client.
    """
    def get(self, request, format=None):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetail(MixinAuth): 
    """
    Retrieve, update or delete a client instance.
    """
    def get_object(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        client = self.get_object(pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        client = self.get_object(pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClientReportList(MixinAuth):
    """
    List report with all clients info.
    """
    def get(self, request, format=None): 
        result = []
        for c in Client.objects.all():
            result.append({
                'id': c.pk,
                'document': c.document,
                'first_name': c.first_name,
                'last_name': c.last_name,
                'email': c.email,
                'bills_total': len(self.getBillsByUser(pk=c.pk))
            })
        return HttpResponse(result)

    def getBillsByUser(self, pk):
        return Bill.objects.filter(client_id=pk)