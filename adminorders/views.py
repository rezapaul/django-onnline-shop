from django.shortcuts import render ,redirect ,get_list_or_404
from accounts.models import Billing
from order.models import Order_done , User_orders
from django.contrib.admin.views.decorators import staff_member_required






@staff_member_required()
def allorders(request):
    orders = User_orders.objects.order_by('-id')
    for product in orders:
        userid = product.user_id

    userinfo = Billing.objects.all().filter(user_id=userid)
    context = {
        'orders' :orders ,
        'userinfo' : userinfo ,
    }

    return render(request,'adminorders/adminorders.html',context)







@staff_member_required()
def orderdetail(request,bought_id):

    orders = get_list_or_404(Order_done ,buy_id=bought_id)
    for product in orders:
        userid = product.user_id

    userinfo = Billing.objects.all().filter(user_id=userid)
    
    for product in orders :
            total = product.product_total + 0
    if total - 10 >= 500 :
        shipment = 1
    else :
        shipment = 0    
    
    context = {
        'orders' : orders ,
        'total' : total ,
        'buy_id' : bought_id ,
        'shipment' : shipment ,
        'userinfo' : userinfo ,
    }
    print(userinfo)
    return render(request,'adminorders/orderdetail.html',context)