from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import LoginSerializer,SignupSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
import random
import os
from .models import Otp
from django.template import loader
from django.core.mail import EmailMultiAlternatives,send_mail
from django.conf import settings
from .serializers import VerifyEmailSerializer,ResendEmailSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
# from deal_tracker.celery import send_otp_mail
# from deal_tracker.celery import setup_task
from django.contrib.auth import get_user_model

User=get_user_model()


# def generate_otp():
#     return random.randint(10000,99999)

# def send_otp_mail(user):
#     try:
#         otp=user.otp  
#     except Exception as e:
#         otp=Otp()
#         otp.user=user
#     otp.key=generate_otp()
#     print(otp.key)
#     otp.save()
#     print("DONE OTP")
#     email_template_html=loader.render_to_string('email_activate.html',
#     context={'otp':otp})
#     subject="Activate Account"
#     recipient_list=[user.email]
#     email_from=settings.EMAIL_HOST_USER
#     email_message=EmailMultiAlternatives(subject=subject
#     ,body="This is the otp",from_email=email_from
#     ,to=recipient_list)
#     email_message.attach_alternative(email_template_html,
#     'text/html')
#     email_message.send(fail_silently=True)



# Create your views here.
class LoginView(APIView):
    def post(self,request):
        data=request.data 
        serializer=LoginSerializer(data=data)
        if(not serializer.is_valid()):
            print(serializer.errors)
            return Response(serializer.errors,status=400)
        print('Serialized')
        user=serializer.validated_data['user']
        if(not serializer.validated_data['is_active']):
            pass
            # send_otp_mail.delay(user.pk)
        return Response({'access_token':serializer.validated_data['access_token'],
        'refresh_token':serializer.validated_data['refresh_token'],
        'is_active':serializer.validated_data['is_active']})



class SignupView(APIView):
    def post(self,request):
        data=request.data
        serializer=SignupSerializer(data=data)
        if(not serializer.is_valid()):

            return Response(serializer.errors,400)

        user=serializer.validated_data['user_profile']
        print(f"SENDING MAIL to {user.pk} ")
        # send_otp_mail.delay(user.pk)
        print("SENT MAIL")
        # send_mail('OTP Activate',"hi",settings.EMAIL_HOST_USER,
        # ['dayodele89@gmail.com'],fail_silently=False)
        return Response(status=200)






class VerifyEmailView(APIView):
    def post(self,request):
        data=request.data
        serializer=VerifyEmailSerializer(data=data)
        if(not serializer.is_valid()):
            return Response(serializer.errors,status=400)
        
        print(f"VALIDATED {serializer.validated_data}")
        try:
            otp=Otp.objects.get(key=serializer.validated_data['key'])
            user=otp.user
            user.is_active=True
            user.save()
            
            refresh_token_obj=RefreshToken.for_user(user=user)
            access_token=str(refresh_token_obj.access_token)
            refresh_token=str(refresh_token_obj)

            return Response({'access_token':access_token,
            'refresh_token':refresh_token,'is_active':True})
        except Otp.DoesNotExist as e:
            return Response(status=400,data={'otp_invalid':True})

class ResendOTPView(APIView):
    def post(self,request):
        data=request.data
        serializer=ResendEmailSerializer(data=data)
        if(not serializer.is_valid()):
            return Response(data=serializer.errors,status=400)

        user=serializer.validated_data['user']
        # send_otp_mail(user=user)
        return Response(status=200)