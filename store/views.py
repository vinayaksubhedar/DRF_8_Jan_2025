from django.shortcuts import render
from django.http import HttpResponse
from store.models import *
from django.db.models import Prefetch
from django.db.models import Func, F,Value
from django.db.models.functions import Concat

# Create your views here.

def home(request):
    return render(request,"store\index.html",{"name" : "Vinayak"})

def products(request):
    query_set = Product.objects.all()
    products = list(query_set)
    return render(request,"store\products.html",{"name" : "Vinayak","products" : products})

def products_cofee(request):
    query_set = Product.objects.filter(title__icontains='Coffee')
    products = list(query_set)
    return render(request,"store\products.html",{"name" : "Vinayak","products" : products})


def products_year(request,year):
    query_set = Product.objects.filter(last_update__year=int(year))
    products = list(query_set)
    return render(request,"store\products.html",{"products":products,"year":year})


def product_collection(request):
    query_set = Product.objects.select_related('collection').all()
    #query_set = Product.objects.all()
    products = list(query_set)
    return render(request,"store\products_collections.html",{"products":products})

def collections(request):
    queryset = Collection.objects.prefetch_related("featured_product").all()
    collections = list(queryset)
    return render(request,"store\collections.html",{"collections" : collections})

def top_orders(request):
#     #return HttpResponse("Top Orders")
#     #query_set = OrderItem.objects.select_related("order").select_related("product").all()
#     query_set = (
#     Order.objects.prefetch_related(
#         Prefetch(
#             'orderitem',
#             queryset=OrderItem.objects.select_related('product')
#         )
#     )
#     .select_related('customer')
#     .order_by('-placed_at')[:5]
# )
#     orders = list(query_set)
    # queryset = Order.objects.select_related("customer").annotate(
    #     full_name=Func(F('customer__first_name'),Value("****"),F('customer__last_name'),function="CONCAT")
    #     ).prefetch_related("orderitem_set__product").order_by("-placed_at")[:5]
    
    queryset = Order.objects.select_related("customer").annotate(
        full_name=Concat('customer__first_name',Value("****"),"customer__last_name")
    ).prefetch_related("orderitem_set__product").order_by("-placed_at")[:5]
    orders = list(queryset)
    return render(request,"store/top_orders.html",{"orders":orders})
