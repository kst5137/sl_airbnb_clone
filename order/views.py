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
from shop.models import Product



def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)

            # order.user = request.user
            # order.product = request.product
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


class OrderCreateAjaxView(View,Product):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({"authenticated": False}, status=403)

        product = Product.objects.all()

        cart = Cart(request)
        print(cart)

        print('_________________________')
        for item in cart:
            print(item)
            product_name = item['product']
        print(product_name)
        form = OrderCreateForm(request.POST)
        # print(form)
        # 실패목록
        # print(request.GET.all('cart'))
        # print(cart.session['products'])
        # session_key = cart.session.session_key
        # print(session_key)
        # print(request.session.get('cart'))   = None
        # print(Cart) = <class 'cart.cart.Cart'>
        # print(cart['product']) = TypeError: 'Cart' object is not subscriptable
        # cart['product']의 형태가 아니라 cart.product 이런식으로 안해서 일어나는 오류
        # print(cart.products) = AttributeError: 'Cart' object has no attribute 'products'

        print("post 통과")
        # print(form)
        if form.is_valid():
            print("is_valid 통과")


            order = form.save(commit=False)
            print("form save 통과")
            # print(request.user.u_nickname)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.amount
            # order.username = request.user.u_nickname
            # print(User.objects.get(u_nickname=request.user.u_nickname))
            order.username = User.objects.get(u_nickname=request.user.u_nickname)
            order.product = Product.objects.get(name=product_name)
            # order.product = Product.objects.get(name=Product.name)
            # print(order.product)
            # 새로운 오류
            # order.product = Product.name = ValueError: Cannot assign "<django.db.models.query_utils.DeferredAttribute object at 0x000002080E84ED60>": "Order.product" must be a "Product" instance.
            # order.product = Product.objects.get(id=form.product_id)
            # order.product = request.session.product
            # print(order.product)
            order.save()

            # print('product:',order.product)

            print("order save 1 통과")
            # order.save()
            # print(cart[1])
            for item in cart:

                # 프랑스라고 출력은 되는데 그럼 cart안에도 있는게 아닌가?
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