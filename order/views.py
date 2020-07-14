from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required 
from .models import Cart_Added , Order_done ,User_orders
from django.contrib import messages
from accounts.models import Billing ,Curency
from random import randint







@login_required(login_url='login')
def cart(request):
    user_id = request.user.id
    products = Cart_Added.objects.order_by('-addtocart_date').filter(is_active=True,is_ordering=False,is_done=False,user_id=user_id)
    subtotal = 0
    for product in products:
        subtotal = subtotal + product.product_total
    
    context = {
        'products' : products ,
        'subtotal' : subtotal ,
    }

    return render(request,'order/cart.html',context)






@login_required(login_url='login')
def deletefromcart(request):
    if request.method == 'POST' :
        user_id = request.user.id
        product_quantity = request.POST['product_quantity']
        product_name = request.POST['product_name']
        product_id = request.POST['product_id']
        product_size = request.POST['product_size']
        product_total = request.POST['product_total']
        p_id = request.POST['p_id']
        product = Cart_Added.objects.order_by('addtocart_date').filter(id=p_id,product_id__exact=product_id,is_active=True,is_ordering=False,
                                                                product_quantity__exact=product_quantity,is_done=False,user_id=user_id,product_size__exact=product_size ,product_total__exact=product_total)
        product.delete()
        messages.success(request, " " + product_name + " (" + product_size + ")"+ " removed")
        return redirect('cart')







@login_required(login_url='login')
def checkout(request):

    curency = Curency.objects.get(user_username__exact=request.user.username)
    products = Cart_Added.objects.order_by('addtocart_date').filter(is_active=True , is_ordering=False ,is_done=False ,user_id=request.user.id)
    subtotal = 0
    for product in products:
        subtotal = subtotal + product.product_total

    users_bill = Billing.objects.all().filter(user_id=request.user.id)
    
    if subtotal > 500.0 :
        order_total = subtotal + 0
    else :     
        order_total = subtotal + 10
        
    context = {
        'billing' : users_bill,
        'products' : products ,
        'subtotal' :subtotal ,
        'order_total' : order_total ,
        'curency' : curency ,

    }

    return render(request,'order/checkout.html',context)






@login_required(login_url='login')
def confermation(request):
    return render(request,'order/confermation.html')        






@login_required(login_url='login')
def placeorder(request):

    if request.method == 'POST' :
        user_id = request.user.id
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        street_address = request.POST['street_address']
        apartment_address = request.POST['apartment_address']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        email = request.POST['email']
        phone = request.POST['phone']
        curency = int(request.POST['curency'])
        

        """Person billing info """

        if Billing.objects.all().filter(user_id=user_id).exists():
            billing = Billing.objects.all().filter(user_id=user_id)
            billing.update(first_name=first_name ,last_name=last_name ,street_address=street_address ,apartment_address=apartment_address,state=state ,zipcode=zipcode
                          ,email=email ,phone=phone)
            
        else :
            billing = Billing(user_id=user_id ,first_name=first_name ,last_name=last_name ,street_address=street_address ,apartment_address=apartment_address,
                            state=state ,zipcode=zipcode ,email=email ,phone=phone)
            billing.save()
            
        
        
        """Calculate Total products """

        products = Cart_Added.objects.order_by('addtocart_date').filter(is_active=True , is_ordering=False ,is_done=False ,user_id=request.user.id)
        subtotal = 0
        for product in products:
            subtotal = subtotal + product.product_total

        users_bill = Billing.objects.all().filter(user_id=request.user.id)
        
        if subtotal > 500.0 :
            order_total = subtotal + 0
        else :     
            order_total = subtotal + 10
        
        
        """Minus Order total from wallet  """

        now_curency = curency
        if now_curency > order_total :
            finall_curency = now_curency - order_total
            wallet_curency = Curency.objects.filter(user_username__exact=request.user.username).update(curency=finall_curency)



            """Add to Order-Done list  """

            a=randint(0,1000000)
            for p in products :
                order_done = Order_done(buy_id=a ,user_id=request.user.id ,product_id=p.product_id ,product_name=p.product_name,
                                        product_size=p.product_size,product_quantity=p.product_quantity,product_price=p.product_price,
                                        product_total=order_total
                                        )
                order_done.save()  

            products.update(is_active=False , is_ordering=True , is_done=True)    
            
            user_orders = User_orders(user_id=request.user.id , buy_id=a)
            user_orders.save()

            return redirect('confermation') 
        else :
            messages.error(request,'Your wallet curency is fewer than order total')
            return redirect('checkout')    








@login_required(login_url='login')
def deleteallcart(request):
    if request.method == 'POST' :
        user_id = request.user.id
        product = Cart_Added.objects.order_by('-addtocart_date').filter(is_done=False,is_active=True,is_ordering=False,user_id=user_id)
        product.delete()
        messages.success(request, " " + " All removed")
        return redirect('cart')