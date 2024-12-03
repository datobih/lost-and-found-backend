from rest_framework.test import APITestCase
from django.urls import reverse
# Create your tests here.
class BaseTestCase(APITestCase):

    def setUp(self):
        self.test_create_lost_item()
    

    def test_create_lost_item(self):
        url = reverse('create-lost-item')
        img = open('C:/Users/DAVID/Documents/Scanned Documents/NIN.jpg','rb')
        data = {'name':'DCD','description':"dcvev",'image':img}
        response  = self.client.post(path = url,data=data)
        print(response.json())
        return 
    
    def test_get_lost_items(self):
        url = reverse('lost-items')
        response = self.client.get(path= url)
        print(response.json())
        return
    
    def test_found_item(self):
        url = reverse('item-found')
        response = self.client.post(path =url,data={'ids':1})
        print(response.json())
        return

    

