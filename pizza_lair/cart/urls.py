from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # http://localhost:8000/myProfile
    path('', views.index, name="index"),
    path('addToCart', views.add_to_cart, name="addToCart"),
    path('clearCart',views.clear_cart),
    path('delCart/<int:item_id>', views.delete_item)
]