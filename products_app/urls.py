from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path("", views.index, name='index'),
    path("products/", views.products_list, name='products'),
    path("login/", LoginView.as_view(), name='login'),
    path("logoout/", LogoutView.as_view(), name='logout'),
    path("profile/", views.profile, name='profile'),
    path("password_change/", PasswordChangeView.as_view(), name='password_change'),
    path("password_change_done/", PasswordChangeDoneView.as_view(), name='password_change_done'),
    path("password/reset/", PasswordResetView.as_view(), name='password_reset'),
    path("password/reset/done/", PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r"^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$", PasswordResetConfirmView.as_view(),
            name='password_reset_confirm'),
    path("password/reset/complete/", PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path("category/<int:pk>/", views.category_detail, name='category_detail'),
    path("product/<int:pk>/", views.product_detail, name='product_detail'),
    path("register/", views.register, name='register'),
    path("register/success/", views.register_success, name="register_success"),
    path('delete/<int:pk>/', views.confirm_delete, name="confirm_delete"),
    path("change_product/<int:pk>/", views.change_product, name='change_product'),
    path("create_product/", views.create_product, name="create_product"),
    path("admin_panel/", views.admin_panel, name="admin_panel"),
    path("create_category/", views.create_category, name="create_category"),
]
