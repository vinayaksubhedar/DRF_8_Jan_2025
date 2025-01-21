from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from store.models import *
from django.db.models import Prefetch
from django.db.models import Func, F,Value
from django.db.models.functions import Concat
from .serializers import ProductSerializer
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request

# Create your views here.
@api_view(['GET', 'POST'])
def product_api(request:Request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






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
