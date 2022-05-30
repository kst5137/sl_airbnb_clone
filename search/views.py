from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def searchResult(request):
  products = None
  query = None
  global posts
  if 'q' in request.GET:
    query = request.GET.get('q')

    products = Product.objects.all().filter(Q(p_name__contains=query) | Q(content__contains=query) | Q(price__contains=query) | Q(writer_id__username__contains=query))

    paginator = Paginator(products, 3)
    page = int(request.GET.get('page', 1))

    posts = paginator.get_page(page)




    return render(request,'search/search_list.html',{'query':query, 'products': products, 'posts':posts})







def get_queryset(self):
  search_keyword = self.GET.get('q','')
  product_list = Product.objects.oreder_by('-id')

  if search_keyword:
    if len(search_keyword) > 1 :
      search_product_list = product_list.filter(Q(p_name__contains=search_keyword) | Q(content__contains=search_keyword) | Q(price__contains=search_keyword) | Q(writer_id__username__contains=search_keyword))

      return search_product_list

    else:
      messages.error(self.request,'검색어를 두글자 이상 입력해주세요.')


  return product_list


def get_context_dat(self,**kwargs):
  search_keyword = self.GET.get('q','')

  if len(search_keyword) > 1 :

    context = {
      'q': search_keyword
    }
  return context