from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_coffee, name='all_coffee'),
    path('<int:coffee_id>/', views.coffee_detail, name='coffee_detail'),
]
