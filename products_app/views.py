from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from cart.froms import CartAddProductForm
from .forms import UserForm, UserRegistrationForm, ProductForm, CreateProductForm, CreateCategory
from .models import Product, ProductCategory
from django.views.generic import TemplateView
from cart.cart import Cart


def products_list(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    cart_product_form = CartAddProductForm()
    paginator = Paginator(products, 3)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page_obg = paginator.get_page(page_num)
    return render(request, 'products/products.html',
                  context={'products': page_obg.object_list,
                           'categories': categories,
                           "cart_product_form": cart_product_form,
                           "page": page_obg})


def index(request):
    return render(request, 'products/index.html')


@login_required
def profile(request):
    form = UserForm(instance=request.user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно изменены.')
        else:
            messages.error(request, 'Ошибка, проверьте правильность введенных данных')
    return render(request, 'users/profile.html', context={'form': form})


def category_detail(request, pk):
    category = ProductCategory.objects.get(pk=pk)
    categories = ProductCategory.objects.all()
    products = Product.objects.filter(category_id=pk)
    cart_product_form = CartAddProductForm()
    paginator = Paginator(products, 3)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page_obg = paginator.get_page(page_num)
    return render(request, 'products/category_detail.html',
                  context={'categories': categories, 'products': page_obg.object_list, 'pk': pk,
                           "cart_product_form": cart_product_form, "page": page_obg, "category": category})


def product_detail(request, pk):
    categories = ProductCategory.objects.all()
    product = Product.objects.get(pk=pk)
    cart_product_form = CartAddProductForm()
    cnt = [i for i in range(1, product.quantity + 1)]
    return render(request, 'products/detail.html',
                  context={"categories": categories, "product": product, "cart_product_form": cart_product_form,
                           "cnt": cnt})


def register(request):
    if not request.user.is_authenticated:
        form = UserRegistrationForm()
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                if data['password1'] != data['password2']:
                    messages.error(request, "Пароли не совпадают, попробуйте снова")
                else:
                    new_user = form.save(commit=False)
                    new_user.set_password(data['password1'])
                    new_user.save()
                    return redirect("register_success")
        return render(request, "register/register.html", context={"form": form})
    else:
        return redirect("index")


class RegisterSuccess(TemplateView):
    template_name = "register/success.html"


def register_success(request):
    if not request.user.is_authenticated:
        return render(request, "register/success.html")
    else:
        return redirect("index")


def confirm_delete(request, pk):
    cart = Cart(request)
    product = Product.objects.get(pk=pk)
    cart.remove(product)
    product.delete()
    return redirect("products")


def change_product(request, pk):
    if request.user.is_superuser:
        product = Product.objects.get(pk=pk)
        form = ProductForm(instance=product)
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                messages.success(request, "Данные успешно изменены")
            else:
                messages.error(request, "Ошибка, проверьте корректность веденных данных")
        return render(request, "products/change_product.html", context={"form": form, "product": product})
    else:
        return redirect("products")


def create_product(request):
    if request.user.is_superuser:
        form = CreateProductForm()
        if request.method == 'POST':
            form = CreateProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save()
                return render(request, "products/create_product_success.html", context={"product": product})
        return render(request, "products/create_product.html", context={"form": form})
    else:
        return redirect("products")


def admin_panel(request):
    return render(request, "admin/admin_panel.html")


def create_category(request):
    form = CreateCategory()
    if request.method == 'POST':
        form = CreateCategory(request.POST)
        if form.is_valid:
            form.save()
            return redirect("products")
    return render(request, "products/create_category.html", context={"form": form})
