from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from . models import Coupon ,Used_coupon
from accounts.models import Curency
from django.contrib import messages



@login_required(login_url='login')
def coupon(request):

    if request.method == 'POST':
        code = request.POST['code']

        if Coupon.objects.all().filter(name__exact=code).exists():
            coupons = Coupon.objects.get(name__exact=code)
            if coupons.is_active :
                if Used_coupon.objects.all().filter(user_id=request.user.id,name__exact=code).exists():
                    messages.error(request," You used This coupon")
                    return redirect('cart')

                else:
                    gift = coupons.currency
                    user_curency = Curency.objects.get(user_username__exact=request.user.username)
                    now_curency = user_curency.curency 
                    new_curency = now_curency + gift
                    Curency.objects.filter(user_username__exact=request.user.username).update(curency=new_curency)
                    add_used = Used_coupon(user_id=request.user.id,name=code)
                    add_used.save()
                    messages.success(request," : " + " Your money increased as $" + str(gift))
                    return redirect('cart')

            else :
                messages.error(request," Expired ")
                return redirect('cart') 

        else:

            messages.error(request," Coupon doesnt exists ")
            return redirect('cart')

