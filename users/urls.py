from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('modify/', usermodify, name='user_modify'),
    path('host_main/', host_main, name='host_main'),
    # path('/create_product', create_product, name='create_product'),
    # path('<slug:category_slug>/', product_in_category, name='product_in_category'),
    # path('<int:id>/<product_slug>/', product_detail, name='product_detail'),
]
