from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Breeds
from .serializers import BreedsSerializer

class BreedsAPIView(APIView):
    def get(self, request):
        result = Breeds.objects.all().values()
        return Response({'title': list(result)})

    def post(self, request):
        serializer = BreedsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Breeds.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            category_id=request.data['category_id']
        )
        return Response({'post': BreedsSerializer(post_new).data})


# class BreedsAPIView(generics.ListAPIView):
#     queryset = Breeds.objects.all()
#     serializer_class = BreedsSerializer
