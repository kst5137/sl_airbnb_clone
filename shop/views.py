from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from cart.forms import AddProductForm
from .forms import *
from django.db import transaction
from django.http import HttpResponseNotAllowed
from django.core.paginator import Paginator
#
from allauth.account.signals import user_signed_up
from django.dispatch import receiver


def func2(abcde) :
    return render(abcde, 'templates/users01/login.html')


# def home():
#     return render(request, 'shop/list.html', {'current_category': current_category,
#                                               'categories': categories,
#                                               'products': products,
#                                               'posts': posts
def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(display=True)

    paginator = Paginator(products,3)
    page = request.GET.get('page')
    posts=paginator.get_page(page)


    if category_slug:
        current_category = get_object_or_404(Category, c_slug=category_slug)
        products = products.filter(category=current_category)


    return render(request, 'shop/list.html', {'current_category': current_category,
                                              'categories': categories,
                                              'products': products,

                                              })


def product_in_category_test(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(display=True)

    paginator = Paginator(products,3)
    page = int(request.GET.get('page',1))
    posts=paginator.get_page(page)


    if category_slug:
        current_category = get_object_or_404(Category, c_slug=category_slug)
        products = products.filter(category=current_category)
        paginator = Paginator(products, 3)
        page = int(request.GET.get('page',1))
        posts = paginator.get_page(page)


    return render(request, 'shop/list_test.html', {'current_category': current_category,
                                              'categories': categories,
                                              'products': products,
                                              'posts' : posts
                                              })



def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, p_slug=product_slug)
    add_to_cart = AddProductForm(initial={'quantity': 1})
    return render(request, 'shop/detail.html', {'product': product, 'add_to_cart': add_to_cart})


    # login_session = request.session.get('login_session', '')
    # context = {'login_session':login_session}
    #
    # product = get_object_or_404(Product, id=id, slug=product_slug)
    # context['product'] = product
    # inquiry = get_object_or_404(Inquiry, id=id)
    # context['inquiry'] = inquiry
    # if product.writer.user_id == login_session:
    #     context['writer'] = True
    # else :
    #     context['writer'] = False


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
            product.writer = request.user
            with transaction.atomic():
                product.save()
                image_formset.instance = product
                image_formset.save()
                return redirect(product)
    else:
        product_form = ProductForm()
        image_formset = ImageFormSet()

    context = {'product_form' : product_form, 'image_formset' : image_formset}
    return render(request, 'shop/create_product.html', context)

@login_required
def register_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.writer == request.user or request.user.is_staff == '1':
        if request.method == "GET":
            form = ProductForm(instance=product)
            image_formset = ImageFormSet()
            return render(request, 'shop/register_product.html', {'form': form, 'image_formset':image_formset})
        else:
            form = RegisterProductForm(request.POST, instance=product)
            image_formset = ImageFormSet(request.POST, request.FILES)
            print('POST~!', form)
            if form.is_valid():
                print('valid~!')
                product.category = form.cleaned_data['category']
                product.type = form.cleaned_data['type']
                product.p_name = form.cleaned_data['p_name']
                product.p_slug = form.cleaned_data['p_slug']
                product.addr = form.cleaned_data['addr']
                product.content = form.cleaned_data['content']
                product.price = form.cleaned_data['price']
                product.address1 = form.cleaned_data['address1']
                product.address2 = form.cleaned_data['address2']
                product.stock = form.cleaned_data['stock']
                product.size = form.cleaned_data['size']
                product.attribute = form.cleaned_data['attribute']
                product.facility = form.cleaned_data['facility']
                product.rule = form.cleaned_data['rule']
                product.safety = form.cleaned_data['safety']
                product.display = form.cleaned_data['display']
                product.order = form.cleaned_data['order']
                product.updated = timezone.now()
                with transaction.atomic():
                    product.save()
                    image_formset.instance = product
                    image_formset.save()
                    print(product)
                    return redirect('shop:product_all')
    else :
        messages.error(request, "내 게시글이 아닙니다.")
        return redirect(product)
    return redirect('shop:product_all')

@login_required
def delete_product(request, id) :
    product = get_object_or_404(Product, pk=id)
    if product.writer == request.user or request.user.is_staff == '1':
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return redirect('shop:product_all')
    else :
        messages.error(request, "내 게시글이 아닙니다.")
        return redirect(product)

@login_required
def inquiry_create(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.user = request.user
            inquiry.product = product
            inquiry.save()
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'product': product, 'form': form}
    return render(request, 'shop/detail.html', context)

@login_required
def inquiry_delete(request, id) :
    inquiry = get_object_or_404(Inquiry, id=id)
    product = get_object_or_404(Product, id=inquiry.product.id)
    if inquiry.user == request.user or request.user.is_staff == '1':
        inquiry.delete()
        return redirect(product)
    else :
        messages.error(request, "내 문의글이 아닙니다.")
        return redirect(product)

