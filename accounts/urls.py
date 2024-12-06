from django.urls import path
from . import views

urlpatterns = [

    path('signup/',views.SignupView.as_view(),name='signup'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('profile/',views.GetProfileView.as_view(),name = 'profile'),
    path('delete-account/',views.DeleteAccountView.as_view(),name='delete-account')
]