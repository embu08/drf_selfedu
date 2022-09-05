from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Breeds
from .serializers import BreedsSerializer


class BreedsModelViewSet(viewsets.ModelViewSet):
    queryset = Breeds.objects.all()
    serializer_class = BreedsSerializer
