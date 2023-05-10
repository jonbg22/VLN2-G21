from django.urls import path
from . import views

urlpatterns = [
    path('pizzas', views.pizzas, name="pizzas"),
    path('pizzas/<int:id>', views.get_pizza_by_id, name="pizza_details"),
    path('sides', views.sides, name="sides"),
    path('sides/<int:id>', views.get_side_by_id, name="side_details"),
    path('drinks', views.drinks, name="drinks"),
    path('drinks/<int:id>', views.get_drink_by_id, name="drink_details"),
]
