from django.shortcuts import render 
from .serializers import ProductSerializer
from products.models import Product
from rest_framework import status
from rest_framework.decorators import api_view ,permission_classes , throttle_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser ,IsAuthenticated 
from rest_framework.throttling import UserRateThrottle






@api_view(['GET','POST'])
@permission_classes([IsAdminUser])
@throttle_classes([UserRateThrottle])
def products(request):
    if request.method == 'GET' :
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=201)
        else :
            return Response(serializer.errors , status=400)    




@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAdminUser])
@throttle_classes([UserRateThrottle])
def product(request,product_id):
    try :
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist :
        return Response("Not Found" , status = 404)

    if request.method == 'GET' :
        serializer = ProductSerializer(product)
        return Response(serializer.data)   

    elif request.method == 'PUT' :
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status = 400)  

    elif request.method == 'DELETE' :
        product.delete()
        return Response(status = 204)




@api_view(['POST'])
@permission_classes([IsAdminUser])
@throttle_classes([UserRateThrottle])
def search(request):
    if request.method == 'POST':
        products_query = Product.objects.all()

        if 'product_id' in request.POST :
            product_id = request.POST['product_id']
            if product_id :
                products_query = products_query.filter(id__iexact=product_id)

        if 'name' in request.POST :
            name = request.POST['name']
            if name :
                 products_query = products_query.filter(name__icontains=name)

        if 'price' in request.POST :
            price = request.POST['price']
            if price :
                products_query = products_query.filter(price__iexact=price)

        if 'availibility' in request.POST :
            availibility = request.POST['availibility']
            if availibility :
                products_query = products_query.filter(availibility=availibility)
            
        if 'description' in request.POST :
            description = request.POST['description']
            if description :
                products_query = products_query.filter(description__icontains=description)

        if 'size1' in request.POST :
            size1 = request.POST['size1']
            if size1 :
                products_query = products_query.filter(size1__iexact=size1)

        if 'size2' in request.POST :
            size2 = request.POST['size2']
            if size2 :
                products_query = products_query.filter(size2__iexact=size2)
        
        if 'size3' in request.POST :
            size3 = request.POST['size3']
            if size3 :
                products_query = products_query.filter(size3__iexact=size3)

        if 'size4' in request.POST :
            size4 = request.POST['size4']
            if size4 :
                products_query = products_query.filter(size4__iexact=size4)

        if 'size5' in request.POST :
            size5 = request.POST['size5']
            if size5 :
                products_query = products_query.filter(size5__iexact=size5)
        
        if 'color' in request.POST :
            color = request.POST['color']
            if color :
                products_query = products_query.filter(color__iexact=color)

        if 'is_published' in request.POST :
            is_published = request.POST['is_published']
            if is_published :
                products_query = products_query.filter(is_published=is_published)

   
        if 'ordering' in request.POST :
            ordering = request.POST['ordering']
            if ordering :
                products_query = products_query.order_by(ordering)

        
        if 'price_up' and 'price_down'  in request.POST :
            price_up = request.POST['price_up']
            price_down = request.POST['price_down']
            if price_up and price_down :
                products_query = products_query.filter(price__range=[price_down, price_up])
             
        
    serializer = ProductSerializer(products_query , many=True)
    return Response(serializer.data)    


