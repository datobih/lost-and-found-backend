from rest_framework.test import APITestCase
from django.urls import reverse
# Create your tests here.
class BaseTestCase(APITestCase):

    def setUp(self):
        self.test_create_user()
        self.test_login()
        self.test_create_lost_item()



    def test_create_user(self):
        url = reverse('signup')
        data = {'first_name':'David','last_name':'Ayodele',
                'password':'randomPASS123',
                'phone_number':'+14753658632','confirm_password':'randomPASS123',
                'email':'dicdn@gmail.com'
                }
        response = self.client.post(url,data=data)
        print(response)

    def test_login(self):
        url  = reverse('login')
        data = {'email':"dicdn@gmail.com",'password':'randomPASS123'}
        response = self.client.post(url,data=data)
        self.token = response.json()['access_token']
        print(response.json())

    def test_search_items(self):
        auth_header=f'Bearer {self.token}'
        url = reverse('search-item')
        response = self.client.post(data={'query':"DCE"},path= url,HTTP_AUTHORIZATION=auth_header,
                                           )
        print(response.json())
        return        

    def test_get_profile(self):
        auth_header = f'Bearer {self.token}'
        url  = reverse('profile')
        response = self.client.post(url,HTTP_AUTHORIZATION=auth_header)
        print(response.json())        

    def test_create_lost_item(self):
        url = reverse('create-lost-item')
        img = open('C:/Users/DAVID/Documents/Scanned Documents/NIN.jpg','rb')
        data = {'name':'DCD','description':"dcvev",'image':img,
                'category':'jcdinc','location':'DCE'}
        auth_header=f'Bearer {self.token}'
        response  = self.client.post(path = url,data=data,HTTP_AUTHORIZATION=auth_header,
                                           )
        print(response.json())
        return 
    
    def test_get_lost_items(self):
        auth_header=f'Bearer {self.token}'
        url = reverse('lost-items')
        response = self.client.get(path= url,HTTP_AUTHORIZATION=auth_header,
                                           content_type='application/json')
        print(response.json())
        return
    
    def test_found_item(self):
        url = reverse('item-found')
        response = self.client.post(path =url,data={'ids':1})
        print(response.json())
        return

    

