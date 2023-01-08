from django.contrib import admin
from products.models import ProductCategory, Product, Basket

admin.site.register(ProductCategory)
# admin.site.register(Product)
admin.site.register(Basket)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # pass
    list_display = ('name_product', 'price', 'quantity', 'category')
    fields = ('name_product', 'image', 'description_product', 'short_description', ('price', 'quantity'), 'category')
    readonly_fields = ('short_description',)
    ordering = ('-name_product',)
    search_fields = ('name_product',)


class BasketAdminInLine(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity_in_basket', 'created_timestamp',)
    readonly_fields = ('product', 'created_timestamp',)
    extra = 0
