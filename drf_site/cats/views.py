from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Breeds
from .serializers import BreedsSerializer


class BreedsAPIList(generics.ListCreateAPIView):
    queryset = Breeds.objects.all()
    serializer_class = BreedsSerializer


class BreedsAPIView(APIView):
    def get(self, request):
        result = Breeds.objects.all().values()
        return Response({'title': list(result)})

    def post(self, request):
        serializer = BreedsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "method PUT is not allowed"})
        try:
            instance = Breeds.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        serializer = BreedsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "method DELETE is not allowed"})
        try:
            instance = Breeds.objects.get(pk=pk)
        except:
            return Response({"error": "Objects does not exists or already deleted"})

        instance.delete()

        return Response({"post": "deleted object " + str(pk)})

# class BreedsAPIView(generics.ListAPIView):
#     queryset = Breeds.objects.all()
#     serializer_class = BreedsSerializer
