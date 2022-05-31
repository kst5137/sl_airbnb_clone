from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import datetime
from datetime import datetime
from datetime import timedelta

@csrf_exempt
def searchResult(request):
  products = None
  query = None
  global posts
  if 'q' in request.GET:
    query = request.GET.get('q')


    products = Product.objects.all().filter(Q(p_name__contains=query) | Q(content__contains=query) | Q(price__contains=query) | Q(writer_id__username__contains=query))

    paginator = Paginator(products, 4)
    page = int(request.GET.get('page', 1))
    posts = paginator.get_page(page)
    return render(request,'search/search_list.html',{'query':query, 'products': products, 'posts':posts})




def calenderResult(request):
  if 'date' in request.GET and 'date2' in request.GET:
    checkin = (request.GET.get('date'))
    checkout = (request.GET.get('date2'))
    want_checkin = datetime.strptime(checkin,"%Y-%m-%d").date()
    want_checkout = datetime.strptime(checkout,"%Y-%m-%d").date()
    products =Product.objects.all().filter((Q(checkin__gte = want_checkin) & Q(checkout__lte=want_checkout)))
    # print(type(want_checkout))
    # print(checkin)
    # print(checkout)
    # print(want_checkout)
    # print('-----------')
    # print(products)
    paginator = Paginator(products, 4)
    page = int(request.GET.get('page', 1))
    posts = paginator.get_page(page)
    return render(request,'search/calender_search_list.html',{'checkin':checkin, 'checkout':checkout, 'products':products, 'posts':posts})

    # products = Product.objects.



