from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ItemSerializer,IDSerialiser
from .models import Item
from rest_framework.response import Response

# Create your views here.

class CreateLostItemView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    def post(self,request):
        data = request.data
        serializer = ItemSerializer(data = data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'Created successfully'},200)
    

class GetLostItemsView(APIView):
    def get(self,request):
        items = Item.objects.filter(is_found=False)
        print(items)
        data = ItemSerializer(items,many = True).data
        return Response({'items': data},200)
    

class ItemFoundView(APIView):
    def post(self,request):
        data = request.data
        serializer = IDSerialiser(data = data)
        if(serializer.is_valid()):
            try:
                item = Item.objects.get(pk = data['id'])
                item.is_found = True
                item.save(update_fields=['is_found'])
                return Response({'message':'success'})
            except Item.DoesNotExist:
                pass
        return Response(data=serializer.errors,status= 400)

    
class GetFoundItems(APIView):
    def get(self,request):
        items = Item.objects.filter(is_found=True)
        data = ItemSerializer(items,many = True).data
        return Response({'items': data},200)
    
