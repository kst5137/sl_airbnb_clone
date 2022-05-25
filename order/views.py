from django.shortcuts import render, get_object_or_404
from .models import *
from cart.cart import Cart
from .forms import *
from django.views.generic.base import View
from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
# pdf를 위한 임포트
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import ListView
from .models import Order

from django.contrib.auth.models import User
# import weasyprint
from users.models import User



def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.amount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity']
                                         )
            cart.clear()
            return render(request, 'order/created_test.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'order/create_test.html', {'cart': cart, 'form': form})


def order_complete(request):
    order_id = request.GET.get('order_id')
    order = Order.objects.get(id=order_id)
    return render(request, 'order/complete.html', {'order': order})


class OrderCreateAjaxView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({"authenticated": False}, status=403)

        cart = Cart(request)
        form = OrderCreateForm(request.POST)
        print("post 통과")
        if form.is_valid():
            print("is_valid 통과")
            order = form.save(commit=False)
            print("form save 통과")
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.amount
            order.username = self.request.user
            print('usernaee:',order.username)
            order.product = self.request.Product
            print('product:',order.product)
            order.save()
            print("order save 통과")
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity']
                                         )
            cart.clear()
            data = {
                "order_id": order.id
            }
            return JsonResponse(data)
        else:
            return JsonResponse({}, status=401)


class OrderCheckoutAjaxView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({"authenticated": False}, status=403)

        order_id = request.POST.get('order_id')
        order = Order.objects.get(id=order_id)
        amount = request.POST.get('amount')

        try:
            merchant_order_id = OrderTransaction.objects.create_new(
                order=order,
                amount=amount
            )
        except:
            merchant_order_id = None

        if merchant_order_id is not None:
            data = {
                "works": True,
                "merchant_id": merchant_order_id
            }
            return JsonResponse(data)
        else:
            return JsonResponse({}, status=401)


class OrderImpAjaxView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({"authenticated": False}, status=403)

        order_id = request.POST.get('order_id')
        order = Order.objects.get(id=order_id)
        merchant_id = request.POST.get('merchant_id')
        imp_id = request.POST.get('imp_id')
        amount = request.POST.get('amount')

        try:
            trans = OrderTransaction.objects.get(
                order=order,
                merchant_order_id=merchant_id,
                amount=amount
            )
        except:
            trans = None

        if trans is not None:
            trans.transaction_id = imp_id
            trans.success = True
            trans.save()
            order.paid = True
            order.save()

            data = {
                "works": True
            }

            return JsonResponse(data)
        else:
            return JsonResponse({}, status=401)


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order/admin/detail.html', {'order': order})


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('order/admin/pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=order_{}.pdf'.format(order.id)
    # weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATICFILES_DIRS[0]+'/css/pdf.css')])
    return response



# 주문내역 조회




# 왜인지 모르지만 구매자 목록
# 후에 buyer detailfh tnwjdgodigka
class order_List(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'order_list'


    def get_queryset(self, **kwargs):

        print(self.request.user.id)
        queryset = Order.objects.filter(username=self.request.user.id)
        return queryset

# 주문내역 조회 다시 도전

class OrderitemList(ListView):
    model = OrderItem
    template_name = 'orderitem_list.html'
    context_object_name = 'orderitem_list'

    # def get_queryset(self, **kwargs):
    #     user = self.request.session.get('user')
    #     print(user)
    # #
    #     queryset = OrderItem.objects.filter(email=self.request.session.get('user'))
    #     return queryset