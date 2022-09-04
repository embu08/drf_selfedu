from django.shortcuts import render
from rest_framework import generics

from .models import Breeds
from .serializers import BreedsSerializer


class BreedsAPIView(generics.ListAPIView):
    queryset = Breeds.objects.all()
    serializer_class = BreedsSerializer
