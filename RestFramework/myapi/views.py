from django.shortcuts import render
from rest_framework.response import Response
from django.http import Http404
from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework import status


class GetView(APIView):
    serializer_class = ProductSerializer
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        snippet = Product.objects.all()
        serializer = ProductSerializer(snippet,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = ProductSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({'ok':'Succesfully created'},status=status.HTTP_200_OK)
        return Response({'Error':'Failed Succesfully'},status=status.HTTP_400_BAD_REQUEST)    


class PutView(APIView):
    serializer_class = ProductSerializer
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
