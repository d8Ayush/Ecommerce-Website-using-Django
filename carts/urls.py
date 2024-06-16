from django.urls import path
from carts.views import  success , cart_page, add_to_cart, remove_cart_item, remove_coupon

urlpatterns = [
    path('add_to_cart/<uid>/', add_to_cart, name='add_to_cart'),
    path('cart_page/', cart_page, name='cart_page'),
    path('remove_cart_item/<cart_item_uid>/', remove_cart_item, name='remove_cart_item'),
    path('remove_coupon/<cart_id>/', remove_coupon, name='remove_coupon'),
        path('success/', success, name='success'),
]
