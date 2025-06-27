from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_touch, name='all_touch'),
    path('<int:touch_id>/', views.touch_detail, name='touch_detail'),
]
