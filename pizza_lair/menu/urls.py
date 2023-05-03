from django.urls import path
from . import views

urlpatterns = [
    path('pizzas', views.index, name="menu-index"),
    path('pizzas/<int:id>', views.get_pizza_by_id, name="pizza_details"),
    path('sides', views.sides, name="sides")
]
