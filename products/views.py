from django.shortcuts import render,get_object_or_404 , redirect
from django.core.paginator import EmptyPage , PageNotAnInteger , Paginator
from .models import Product , Product_comments
from django.contrib import messages
from order.models import Cart_Added



def shop(request):
    
    products = Product.objects.order_by('-product_date').filter(is_published=True)
    paginator = Paginator(products , 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'products' : paged_products
    }

    return render(request,'products/shop.html',context)


def product(request,product_id):
    products = Product.objects.order_by('-product_date').filter(is_published=True)[:5]
    product_info = get_object_or_404(Product ,pk=product_id)
    comments = Product_comments.objects.order_by('-comment_date').filter(product_id=product_id,is_published=True)
    context = {
        'product' : product_info ,
        'comments' : comments , 
        'products' : products ,
    }

    return render(request,'products/product.html',context)




def AddToCart(request):
    if request.method == 'POST':
        user_id = request.user.id
        product_id = request.POST['product_id']
        product_name = request.POST['product_name']
        product_price = float(request.POST['product_price'])
        product_quantity = int(request.POST['product_quantity'])
        product_total = product_price * product_quantity
        product_photo = request.POST['product_photo']
        product_size =request.POST['product_size']

        if Cart_Added.objects.all().filter(user_id=user_id,product_id=product_id,product_name=product_name,product_price=product_price,
                product_size=product_size,is_active=True,is_done=False).exists():
                    messages.error(request,  "   " + product_name + "(" + product_size + ")" + ", already is in Cart")
                    return redirect('product/' + product_id) 
        else :            
            addto = Cart_Added(user_id=user_id,product_id=product_id,product_name=product_name,product_price=product_price,
                            product_quantity=product_quantity,product_total=product_total,product_photo=product_photo,product_size=product_size)
            addto.save()
            
            messages.success(request, " :   " + str(product_quantity) + 'X' + "   " + product_name + ", Added to Cart")
            return redirect('product/' + product_id) 
                 





def addcomment(request):
    if request.method == 'POST':
        product_id = request.POST['pid']
        fullname = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['email']
        content = request.POST['content']
        add = Product_comments(product_id=product_id,fullname=fullname,email=email,phone=phone,content=content)
        add.save()
        messages.success(request,'Your comment will shown after admin viewed')
        return redirect('product/' + product_id)
        



def search(request):

    products_query = Product.objects.order_by('-product_date').filter(is_published=True)
    if 'keywords' in request.GET :
        keywords = request.GET['keywords']
        if keywords :
            products = products_query.filter(name__icontains=keywords)

    context = {
        'products' : products
    }

    return render(request,'products/search.html',context)





def category(request):
    if request.method == "POST":
        cate = int(request.POST['cate'])
        
        products_query = Product.objects.order_by('-product_date').filter(is_published=True,category=cate)
        
        context = {
            'products' : products_query
        }

        return render(request,'products/category.html',context)  
    else :
         return redirect('shop')       