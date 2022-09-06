from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Breeds, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrAdminOrReadOnly
from .serializers import BreedsSerializer


class BreedsAPIList(generics.ListCreateAPIView):
    queryset = Breeds.objects.all()
    serializer_class = BreedsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class BreedsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Breeds.objects.all()
    serializer_class = BreedsSerializer
    permission_classes = (IsOwnerOrAdminOrReadOnly, )


class BreedsAPIDelete(generics.RetrieveDestroyAPIView):
    queryset = Breeds.objects.all()
    serializer_class = BreedsSerializer
    permission_classes = (IsAdminOrReadOnly, )
