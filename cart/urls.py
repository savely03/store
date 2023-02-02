from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('detail/', views.cart_detail, name='cart_detail'),
    path('cart_clear/', views.cart_clear, name='cart_clear'),
    path("cart_decrease/<int:product_id>/", views.cart_decrease, name='cart_decrease'),
]
