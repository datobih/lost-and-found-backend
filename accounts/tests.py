from rest_framework.test import APITestCase
from django.urls import reverse
# Create your tests here.
class BaseTestCase(APITestCase):

    def test_create_user(self):
        url = reverse('signup')
        data = {'first_name':'David','last_name':'Ayodele',
                'password':'randomPASS123','username':'datobi',
                'phone_number':'+14753658632','confirm_password':'randomPASS123',
                'email':'dicdn@gmail.com'
                }
        response = self.client.post(url,data=data)
        print(response)
        
