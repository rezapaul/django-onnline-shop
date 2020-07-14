from django.shortcuts import render,redirect ,get_list_or_404
from django.contrib.auth.models import User
from django.contrib import messages , auth
from django.contrib.auth.decorators import login_required 
from django.core.mail import send_mail
from .models import Favorite ,Curency
from order.models import User_orders ,Order_done






def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2 :
            if User.objects.all().filter(username=username).exists():
                messages.error(request,'username already exists')
                return redirect('register')
            else :
                if User.objects.all().filter(email=email).exists():
                    messages.error(request,'email used before')
                    return redirect('register')
                else :
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
                    user.save()
                    currency = Curency(user_username=username,curency=10)
                    currency.save()
                    messages.success(request,'Successfully registered Now Login')
                    return redirect('login')
        else :
            messages.error(request,'passwords doesnt match')
            return redirect('register')
        messages.success(request,email)
        return redirect('login')
    else :    
        return render(request,'accounts/register.html')








def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username , password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')    






@login_required(login_url='login')
def dashboard(request):

    user_orders = User_orders.objects.all().filter(user_id=request.user.id)

    context = {
        'orders' : user_orders
    }
    return render(request,'accounts/dashboard.html',context)    






@login_required(login_url='login')
def details(request,buy_id):
    orders = get_list_or_404(Order_done ,buy_id=buy_id ,user_id=request.user.id)
    
    for product in orders :
            total = product.product_total + 0

    context = {
        'orders' : orders ,
        'total' : total ,
        'buy_id' : buy_id ,
    }
    return render(request,'accounts/bought.html',context)






def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You logged out successfully')
        return redirect('index') 



@login_required(login_url='login')
def addtofavorite(request):
    if request.method == 'POST':
        user_id = request.user.id
        product_id = request.POST['product_id']
        product_name = request.POST['product_name']
        product_photo = request.POST['product_photo']
        product_price = request.POST['product_price']
        if Favorite.objects.all().filter(user_id=user_id ,product_id=product_id).exists():
            messages.error(request ," " + product_name + " has added before")
            return redirect('/shop/product/'+product_id)
        else :    
            favorite = Favorite(user_id=user_id , product_id=product_id, product_name=product_name , product_photo=product_photo , product_price=product_price)
            favorite.save()
            messages.success(request ," " + product_name + " added to your favorites")
            return redirect('/shop/product/'+product_id)






@login_required(login_url='login')
def favorite_inf(request):

    favorites = Favorite.objects.all().filter(user_id=request.user.id)
    context = {
        'favorites' : favorites
    }      

    return render(request,'accounts/favorite.html',context)  





@login_required(login_url='login')
def removefavorite(request):
    if request.method == 'POST' :
        user_id = request.user.id
        product_id = request.POST['product_id']
        product_name = request.POST['product_name']
        f_id = request.POST['f_id']
        fav = Favorite.objects.all().filter(id=f_id,product_name=product_name,product_id=product_id)
        fav.delete()
        messages.success(request," :" + product_name + " removed from favorites" )
        return redirect('favorites')






@login_required(login_url='login')
def wallet(request):
    curency = Curency.objects.get(user_username__exact=request.user.username)

    context = {
        'curency' : curency
    }

    return render(request,'accounts/wallet.html',context) 