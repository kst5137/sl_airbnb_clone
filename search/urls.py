from django.urls import path
from .views import *

app_name = 'search'

urlpatterns = [
    path('', searchResult, name='searchResult'),
    path('calender',calenderResult,name='calenderResult')

]
