from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="menu-index"),
    path('pizza/<int:id>', views.get_pizza_by_id, name="pizza_details")
]
