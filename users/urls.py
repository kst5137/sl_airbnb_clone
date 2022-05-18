from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('<int:pk>/', userprofile, name='userprofile'),
    # path('user_modify/', user_modify, name='user_modify'),
    path('host_main/', host_main, name='host_main'),
    path('<int:pk>/modify/', user_modify, name='user_modify')
    # path('/create_product', create_product, name='create_product'),
    # path('<slug:category_slug>/', product_in_category, name='product_in_category'),
    # path('<int:id>/<product_slug>/', product_detail, name='product_detail'),
]
