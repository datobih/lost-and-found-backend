from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    contact = serializers.CharField(source = 'posted_by.phone_number',read_only=True)

    class Meta:
        model = Item
        fields = '__all__'




class IDSerialiser(serializers.Serializer):
    id = serializers.CharField()




class QuerySerializer(serializers.Serializer):
    query = serializers.CharField()