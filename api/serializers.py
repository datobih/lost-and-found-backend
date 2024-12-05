from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class IDSerialiser(serializers.Serializer):
    id = serializers.CharField()




class QuerySerializer(serializers.Serializer):
    query = serializers.CharField()