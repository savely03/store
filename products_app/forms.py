import re
from django import forms
from django.contrib.auth.models import User
from .models import Product, ProductCategory


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email')


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "first_name", "email")

    def clean(self):
        clean_data = self.cleaned_data
        if User.objects.filter(username=clean_data["username"]).exists():
            self.add_error("username", "Данное имя пользователя уже существует")
        if clean_data.get("email") is not None:
            if User.objects.filter(email=clean_data["email"]).exists():
                self.add_error("email", "Данный email уже существует")
        if not re.match(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8,}$',
                        clean_data['password1']):
            self.add_error("password1", "Пароль должен: "
                                        "содержать не менее 8 символов,"
                                        "содержать хотя бы одну заглавную букву,"
                                        "содержать хотя бы одно число.")
        return self.cleaned_data


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class CreateCategory(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = "__all__"
