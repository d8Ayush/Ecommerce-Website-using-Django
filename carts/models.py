from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from products.models import *
from products.models import Product
from carts.models import Coupon


class Cart(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='carts')
    is_paid = models.BooleanField(default=False)
    coupon = models.ForeignKey(
        Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    razor_pay_order_id = models.CharField(max_length=100, null= True, blank= True)
    razor_pay_payment_id = models.CharField(max_length=100, null= True, blank= True)
    razor_pay_payment_signature = models.CharField(max_length=100, null= True, blank= True)

    def get_cart_total(self):
        cart_items = CartItems.objects.all()
        price = []

        for cart_item in cart_items:
            price.append(cart_item.product.price)

            if cart_item.color_variant:
                color_variant_price = cart_item.color_variant.price
                price.append(color_variant_price)

            if cart_item.size_variant:
                size_variant_price = cart_item.size_variant.price
                price.append(size_variant_price)
        return sum(price)

    def get_cart_total_price_after_coupon(self):
        total = self.get_cart_total()

        if total < self.coupon.minimum_amount:
            return total
        return total - self.coupon.discount_amount


class CartItems(BaseModel):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)
    color_variant = models.ForeignKey(
        ColorVariant, on_delete=models.SET_NULL, null=True, blank=True)
    size_variant = models.ForeignKey(
        SizeVariant, on_delete=models.SET_NULL, null=True, blank=True)

    def get_product_price(self):
        price = [self.product.price]

        if self.color_variant:
            color_variant_price = self.color_variant.price
            price.append(color_variant_price)

        if self.size_variant:
            size_variant_price = self.size_variant.price
            price.append(size_variant_price)

        return sum(price)
