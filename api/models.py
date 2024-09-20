from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()



class Item(models.Model):
    name = models.CharField(max_length=50)
    image  = models.ImageField()
    is_found = models.BooleanField(default=False)
    description = models.TextField()
    date_updated = models.DateTimeField(auto_now=True)
