from django.contrib import admin
from .models import Customer,Product,Collection,Order,OrderItem,Promotion
from django.db.models import Count

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ["id","customer"]    

class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","order_count","email","phone","birth_date","membership","full_name"]
    list_display_links = ["full_name"]
    ordering = ["-membership"]
    search_fields = ["email"]
    #exclude = ["birth_date"]

    @admin.display(description="New Name") # Descritpion will be shown as a Label to Field
    def full_name(self,obj:Customer):
        return obj.first_name + "" + obj.last_name

    @admin.display(ordering='order_count')
    def order_count(self,obj:Order):
        return obj.order_count
    

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            order_count=Count('order')
        )


#admin.site.register(Customer,CustomerAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Product)
admin.site.register(Collection)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)



