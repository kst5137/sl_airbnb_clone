from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
def searchResult(request):
  products = None
  query = None
  if 'q' in request.GET:
    query = request.GET.get('q')
    products = Product.objects.all().filter(Q(name__contains=query) | Q(content__contains=query) | Q(price__contains=query))



  return render(request,'search/search_list.html',{'query':query, 'products': products})
# def search(request):
#   content_list = Product.objects.all()
#   search = request.GET.get('search','')
#   if search:
#     search_list = content_list.filter(
#       Q(title__icontains = search) | #제목
#       Q(body__icontains = search) | #내용
#       Q(writer__username__icontains = search) #글쓴이
#     )
#   paginator = Paginator(search_list,5)
#   page = request.GET.get('page','')
#   posts = paginator.get_page(page)
#   board = Board.objects.all()
#
#   return render(request, 'search.html',{'posts':posts, 'Board':board, 'search':search})

# from django.contrib import messages
# from django.db.models import Q
#
#
# def get_queryset(self):
#   search_keyword = self.request.GET.get('q', '')
#   search_type = self.request.GET.get('type', '')
#   product_list = Product.objects.order_by('-id')
#
#   if search_keyword:
#     if len(search_keyword) > 1:
#       if search_type == 'all':
#         search_notice_list = product_list.filter(
#           Q(name__icontains=search_keyword) | Q(content__icontains=search_keyword))
#       elif search_type == 'name_content':
#         search_notice_list = product_list.filter(
#           Q(name__icontains=search_keyword) | Q(content__icontains=search_keyword))
#       elif search_type == 'name':
#         search_notice_list = product_list.filter(name__icontains=search_keyword)
#       elif search_type == 'content':
#         search_notice_list = product_list.filter(content__icontains=search_keyword)
#       # elif search_type == 'writer':
#       #   search_notice_list = product_list.filter(writer__user_id__icontains=search_keyword)
#
#       return search_notice_list
#     else:
#       messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
#   return product_list
#
# def get_context_data(self, **kwargs):
#   search_keyword = self.request.GET.get('q', '')
#   search_type = self.request.GET.get('type', '')
#
#   if len(search_keyword) > 1:
#     context = {'q' : search_keyword, 'type' : search_type }
#   return context