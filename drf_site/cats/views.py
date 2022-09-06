from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Breeds, Category
from .serializers import BreedsSerializer


class BreedsModelViewSet(viewsets.ModelViewSet):
    # queryset = Breeds.objects.all()
    serializer_class = BreedsSerializer

    @action(methods=['GET'], detail=True)
    def categories(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'category': cats.name})

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Breeds.objects.all()
        return Breeds.objects.filter(pk=pk)
