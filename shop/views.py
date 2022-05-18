from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from cart.forms import AddProductForm
from .forms import ProductForm, ImageFormSet
from django.db import transaction
import slick
#
from allauth.account.signals import user_signed_up
from django.dispatch import receiver


def func2(abcde) :
    return render(abcde, 'templates/users01/login.html')

def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(request, 'shop/list.html', {'current_category': current_category,
                                              'categories': categories,
                                              'products': products,
                                              })


def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    add_to_cart = AddProductForm(initial={'quantity': 1})
    return render(request, 'shop/detail.html', {'product': product, 'add_to_cart': add_to_cart})

#
# @receiver(user_signed_up)
# def user_signed_up_(**kwargs):
#     user = kwargs['user']
#     extra_data = user.socialaccount_set.filter(provider='naver')[0].extra_data
#     user.last_name = extra_data['name'][0:4]
#     user.first_name = extra_data['name'][4:]
#     user.save()
# from django.shortcuts import render

# Create your views here.

@login_required
def create_product(request) :
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        image_formset = ImageFormSet(request.POST, request.FILES)
        if product_form.is_valid() and image_formset.is_valid():
            product = product_form.save(commit=False)
            product.user = request.user

            with transaction.atomic():
                product.save()
                image_formset.instance = product
                image_formset.save()
                return redirect('shop:product_all')
    else:
        product_form = ProductForm()
        image_formset = ImageFormSet()

    context = {'product_form' : product_form, 'image_formset' : image_formset}
    return render(request, 'shop/create_product.html', context)
