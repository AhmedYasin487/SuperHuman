from django.shortcuts import render,redirect
from .models import Cart
from products.models import Product
from orders.models import Order
# Create your views here.


def cart_home(request):
    cart_obj,new_obj = Cart.objects.new_or_get(request)
    return render(request,'carts/home.html',{'cart':cart_obj})

def cart_update(request):
        # print('this is post',request.POST)
        product_id = request.POST.get('product_id')
        # print('this is id',product_id)
        if product_id is not None:
                try:
                        product_obj = Product.objects.get(id=product_id)
                except Product.DesNotExists:
                        # print('product is gone')
                        return redirect('carts:home')
                cart_obj, new_obj = Cart.objects.new_or_get(request)
                if product_obj in cart_obj.products.all():
                        cart_obj.products.remove(product_obj)
                else:
                        cart_obj.products.add(product_obj)
                request.session['cart_total'] = cart_obj.products.count()
        return redirect('carts:home')

def checkout_home(request):
        cart_obj ,cart_created = Cart.objects.new_or_get(request)
        user = request.user
        billing_profile = None
        order_obj = None
        if cart_created or cart_obj.products.count()== 0:
                return redirect('carts:home')
        else:
                order_obj ,new_order_obj = Order.objects.get_or_create(cart=cart_obj)
        
        if billing_profile is not None:
                order_qs = Order.objects.filter(billiing_profile=billing_profile,cart=cart_obj)
                if order_qs.count() == 1:
                        order_obj=order_qs.first()
                else:
                        old_order_qs = Order.objects.exclude(billing_profile=billing_profile).filter(cart=cart_obj)
                        if old_order_qs.exists():
                                old_order_qs.update()
                        order_by =Order.objects.create(billing_profile=billing_profile,cart=cart_obj)

        return render(request,"carts/checkout.html",{'objects':order_obj})

