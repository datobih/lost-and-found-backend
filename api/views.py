from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ItemSerializer,IDSerialiser
from .models import Item
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.

class CreateLostItemView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    parser_classes = [MultiPartParser, FormParser]
    def post(self,request):
        data = request.data
        data['posted_by'] = request.user.pk
        serializer = ItemSerializer(data = data,context = {'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'Created successfully'},200)
    

class GetLostItemsView(APIView):
    def get(self,request):
        items = Item.objects.filter(is_found=False)
        print(items)
        data = ItemSerializer(items,many = True).data
        return Response(data,200)
    


class GetMyAdsView(APIView):
    def get(self,request):
        items = Item.objects.filter(is_found=False,posted_by = request.user)
        print(items)
        data = ItemSerializer(items,many = True).data
        return Response(data,200)


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
        return Response(data,200)
    
