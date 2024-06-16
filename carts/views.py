from django.shortcuts import render
from .models import Cart, CartItems
from products.models import Product, SizeVariant, Coupon
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import razorpay




def add_to_cart(request, uid):
    variant = request.GET.get('variant')
    user = request.user
    product = Product.objects.get(uid=uid)

    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)
    cart_item = CartItems.objects.create(cart=cart, product=product)

    if variant:
        variant = request.GET.get('variant')
        size_variant = SizeVariant.objects.get(size_name=variant)
        cart_item.size_variant = size_variant
        cart_item.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


from django.conf import settings
def cart_page(request):
    cart_obj = None
    payment = None
    try:
        cart_obj = Cart.objects.get(is_paid=False, user=request.user)
    except Exception as e:
        print(e)
    if request.method == 'POST':
        coupon = request.POST.get('coupon')
        coupon_obj = Coupon.objects.filter(coupon_code__exact=coupon)

        if not coupon_obj.exists():
            messages.warning(request, 'Invalid coupon code.')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])

        if cart_obj.coupon:
            messages.warning(request, 'Coupon already exists.')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])

        if coupon_obj[0].is_expired:
            messages.warning(request, 'Coupon code expired.')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])

        if cart_obj.get_cart_total() < coupon_obj[0].minimum_amount:
            messages.warning(
                request, f'Amount should be greater than {coupon_obj.minimum_amount}')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])

        cart_obj.coupon = coupon_obj[0]
        cart_obj.save()



        messages.success(request, f'Coupon applied.')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    
    if cart_obj and cart_obj.cart_items.exists:
        amount_in_paise = cart_obj.get_cart_total() * 100
        MIN_AMOUNT = 100 

        if amount_in_paise >= MIN_AMOUNT:
            client = razorpay.Client(auth = (settings.KEY , settings.SECRET ))
            try:
                payment = client.order.create({'amount' : cart_obj.get_cart_total() *100 , 'currency' : 'INR' , 'payment_capture' : 1 })
                cart_obj.razor_pay_order_id = payment['id']
                cart_obj.save()

                print('*******')
                print(payment)
                print('*******')
            except razorpay.errors.BadRequestError as e:
                messages.error(request, 'Failed to create Razorpay order. Please try again.')
                print(e)


    
    context = {'cart': cart_obj , 'payment' : payment }
    return render(request, 'carts/cart.html', context)


def remove_cart_item(request, cart_item_uid):
    try:
        cart_item = CartItems.objects.get(uid=cart_item_uid)
        cart_item.delete()
    except Exception as e:
        print(e)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def remove_coupon(request, cart_id):
    cart = Cart.objects.get(uid=cart_id)
    cart.coupon = None
    cart.save()

    messages.success(request, f'Coupon removed.')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])



def success(request):
    order_id = request.GET.get('order_id')
    cart = Cart.objects.get(razor_pay_order_id = order_id)
    cart.is_paid = True
    cart.save()
    return HttpResponse('Payment Success')