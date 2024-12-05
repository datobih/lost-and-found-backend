from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()



class Item(models.Model):
    # CATEGORY_CHOICES=[
    #     ('Jumia','Jumia'),
    #     ('Konga','Konga'),
    #     ('Jiji','Jiji')
    # ]
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image  = models.ImageField()
    is_found = models.BooleanField(default=False)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
