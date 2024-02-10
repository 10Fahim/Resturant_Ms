from django.urls import path

from RestaurantAPP import views

urlpatterns=[
    path('',views.home,name='home'),
    path("list", views.list, name="list"),
    path('add', views.additems, name='add'),
    path('update_food_details/<int:id>', views.updatefooddetails, name='update_food_details'),
    path("delete/<int:id>", views.delete_item, name="delete"),
    path("display", views.displayfun, name='display'),



]