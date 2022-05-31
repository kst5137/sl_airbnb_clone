from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', product_in_category_test, name='product_all'),
    path('create_product/', create_product, name='create_product'),
    path('<category_slug>/', product_in_category_test, name='product_in_category'),
    path('<int:id>/<product_slug>/', product_detail, name='product_detail'),
    path('inquiry/create/<int:id>/', inquiry_create, name='inquiry_create'),
    path('inquiry/delete/<int:id>/', inquiry_delete, name='inquiry_delete'),
    path('register_product/<int:id>/', register_product, name='register_product'),
    path('delete_product/<int:id>/', delete_product, name='delete_product'),
]

#
# urlpatterns = [
#     path('', product_in_category, name='product_all'),
#     path('/create_product', create_product, name='create_product'),
#     path('<slug:category_slug>/', product_in_category, name='product_in_category'),
#     path('<int:id>/<product_slug>/', product_detail, name='product_detail'),
#     path('<int:id>/inquiry_create/', inquiry_create, name='inquiry_create'),
#     path('<int:id>/inquiry_create/<int:inquiry_id>/delete/', inquiry_create, name='inquiry_create'),
#     # path('register_product/<int:product_id>/', register_product, name='register_product'),
# ]