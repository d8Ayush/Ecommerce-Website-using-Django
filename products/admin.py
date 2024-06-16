from django.contrib import admin
from products.models import Category, Product, ProductImage, ColorVariant, SizeVariant, Coupon

admin.site.register(Category)



class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
    readonly_fields = ['img_preview']


@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ['color_name', 'price']
    model = ColorVariant


@admin.register(SizeVariant)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['size_name', 'price']
    model = SizeVariant


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price']
    inlines = [ProductImageAdmin]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['coupon_code', 'discount_amount', 'minimum_amount']
    model = Coupon
