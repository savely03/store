from django.urls import path
from . import views

urlpatterns = [
    # path("", views.order, name='order'),
    path("create/", views.order_create, name='order_create'),
    path("orders/", views.orders, name='orders'),
    path("success/", views.success, name='success'),
    path("make/<int:pk>/", views.make_order, name='make_order'),
    path("watch/<int:pk>/", views.order_watch, name='order_watch'),
]
