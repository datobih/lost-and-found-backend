from rest_framework.test import APITestCase
from django.urls import reverse
# Create your tests here.
class BaseTestCase(APITestCase):

    def setUp(self):

        # self.test_create_user()

        return super().setUp()

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
        print(response.json())
        
