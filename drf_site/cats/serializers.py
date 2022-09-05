from rest_framework import serializers

from .models import Breeds


# class BreedsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Breeds
#         fields = ('title', 'category_id')

class BreedsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()
