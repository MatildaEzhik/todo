from django.urls import path
from dolist import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store/<int:store_id>/', views.store_detail, name='store_detail'),
    path('store/<int:store_id>/category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('store/add/', views.add_store, name='add_store'),
]
