from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "purchaser", "name", "description")
        model = Item
