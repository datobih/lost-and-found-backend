from django.urls import path
from . import views

urlpatterns = [
    
    path('create-lost-item/',view=views.CreateLostItemView.as_view(),name='create-lost-item'),
    path('lost-items/',views.GetLostItemsView.as_view(),name = "lost-items"),
    path("found-items/",views.GetFoundItems.as_view(),name = "found-items"),
    path("item-found/",views.ItemFoundView.as_view(),name= "item-found")

]