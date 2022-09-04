from rest_framework import serializers

from .models import Breeds


class BreedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breeds
        fields = ('title', 'category_id')
