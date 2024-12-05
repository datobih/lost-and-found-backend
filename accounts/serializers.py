from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.db import IntegrityError


User=get_user_model()

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(min_length=8)


    def validate(self, attrs):
        super().validate(attrs)
        user = None
        try:
            user=User.objects.get(email=attrs['email'])
        except User.DoesNotExist :
            raise serializers.ValidationError('User does not exist')

        is_active=user.is_active
        if(not is_active):
            user.is_active=True
            user.save()
        user=authenticate(username=attrs['email'],password=attrs['password'])       
        if(user):
            
            attrs.setdefault('access_token','NOT_ACTIVATED')
            attrs.setdefault('refresh_token','NOT_ACTIVATED')

            if(is_active):
                refresh_token=RefreshToken.for_user(user)
                attrs['access_token']=str(refresh_token.access_token)
                attrs['refresh_token']=str(refresh_token)
            
            
            attrs['is_active']=is_active
            attrs['user']=user
            return attrs
        else:
            print("Invalid credentials")
            raise serializers.ValidationError('Invalid credentials')


class SignupSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()
    confirm_password=serializers.CharField()
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    phone_number = serializers.CharField()

    def validate(self, attrs):
        super().validate(attrs)

        if(not attrs['confirm_password']==attrs['password']):
            raise serializers.ValidationError('Passwords do not match')
        
        if(len(str(attrs['phone_number']))!=12):
            raise serializers.ValidationError("Phone number is not valid")

        del attrs['confirm_password']
        try:
            user=User.objects.create_user(**attrs)
        except IntegrityError as e:
            print(e.__cause__)
            error_message=e.__cause__

            if(str(e.__cause__)=='UNIQUE constraint failed: accounts_user.email'):
                error_message='An account already exists with email'

            if(str(e.__cause__)=='UNIQUE constraint failed: accounts_user.username'):
                error_message='An account already exists with username'
                
            if(str(e.__cause__)=='UNIQUE constraint failed: accounts_user.phone_number'):
                error_message='An account already exists with phone_number'


            raise serializers.ValidationError(f'{error_message}')

        attrs['user_profile']=user

        return attrs



class VerifyEmailSerializer(serializers.Serializer):
    key=serializers.IntegerField()


    def validate(self, attrs):
        return super().validate(attrs)

class ResendEmailSerializer(serializers.Serializer):
    email=serializers.EmailField()


    def validate(self, attrs):
        super().validate(attrs)
        try:
            user=User.objects.get(email=attrs['email'])
        except User.DoesNotExist as e:
            raise serializers.ValidationError("The email provided does not exist")
        
        attrs['user']=user
        return attrs
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email','profile_image']
