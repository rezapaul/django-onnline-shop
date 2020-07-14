from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from products.models import Product



def index(request):
    
    products = Product.objects.order_by('-product_date').filter(is_published=True)[:5]

    context = {
        "products" : products
    }

    return render(request,'pages/index.html',context)


def about(request):
    return render(request,'pages/about.html')


def contact(request):
    return render(request,'pages/contact.html')    


def getcontact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name'] 
        email = request.POST['email']
        subject = request.POST['subject'] 
        content = request.POST['content']  

        contact = Contact(first_name=first_name ,last_name=last_name ,email=email ,subject=subject ,content=content)   
        contact.save()
        messages.success(request, ": " + "Thanks for Contacting Will Seen Soon") 
        return redirect('contact')