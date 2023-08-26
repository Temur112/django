from django.contrib import admin

from .models import Product

# Register your models here.


admin.site.site_header = "Buy and Sell admin panel"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','description',)
    search_fields = ('name',)

    def set_price_to_zero(self, request, queryset):
        queryset.update(price=0)

    actions = ('set_price_to_zero', )

    list_editable = ('price', 'description',)


admin.site.register(Product, ProductAdmin)