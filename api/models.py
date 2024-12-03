from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()



class Item(models.Model):
    # CATEGORY_CHOICES=[
    #     ('Jumia','Jumia'),
    #     ('Konga','Konga'),
    #     ('Jiji','Jiji')
    # ]
    name = models.CharField(max_length=50)
    image  = models.ImageField()
    is_found = models.BooleanField(default=False)
    description = models.TextField()
    date_updated = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
