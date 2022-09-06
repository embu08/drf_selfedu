from rest_framework import serializers

from .models import Breeds


# next 2 classes work the same way
class BreedsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Breeds
        fields = '__all__'
