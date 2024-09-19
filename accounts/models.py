from email.policy import default
from django.db import models
from django.contrib.auth.models import BaseUserManager,PermissionsMixin,AbstractUser
# from authentication.models import Otp
# Create your models here.



class UserManager(BaseUserManager):
    def create_user(self,email,password,**otherfields):
        user=self.model(email=email,**otherfields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,email,password,**otherfields):
        otherfields.setdefault('is_active',True)
        otherfields.setdefault('is_superuser',True)
        otherfields.setdefault('is_staff',True)
        self.create_user(email=email,password=password,**otherfields)


class User(AbstractUser,PermissionsMixin):
    profile_image=models.ImageField(blank=False,null=True)
    is_superuser=models.BooleanField(default=False)
    email=models.EmailField(blank=False,null=False,unique=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name','username']
    objects=UserManager()

    def set_otp(self,key):
        self.otp=key
        self.save()

        
class Otp(models.Model):
    key=models.IntegerField()
    user=models.OneToOneField(to=User,on_delete=models.CASCADE)