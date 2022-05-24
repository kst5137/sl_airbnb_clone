from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [

    path('create_product/', create_product, name='create_product'),
    path('<slug:category_slug>/', product_in_category, name='product_in_category'),
    path('<int:id>/<product_slug>/', product_detail, name='product_detail'),
    path('register_product/<int:product_id>/', register_product, name='register_product'),

    path('', product_in_category, name='product_all'),
]
