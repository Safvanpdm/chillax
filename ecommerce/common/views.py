from django.shortcuts import render,redirect
from .models import Customer , Cart
from ecommerceadmin.models import Products

# Create your views here.

def home(request):
    return render(request,('common/home.html'))

def about(request):
    return render(request,('common/about.html'))

def contact(request):
    return render(request,('common/contact.html'))



def shop(request):

    products =Products.objects.all()

    if request.method == 'POST':

        customer = request.session['customer']

        pid = request.POST['pid']     #pid from hidden input tag

        cart = Cart(customer_id =customer ,product_id = pid )
        cart.save()
        return redirect('common:cart')

    return render(request,'common/shop.html',{'products':products})




def login(request):

    error_msg = ''

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        try:
            customer = Customer.objects.get(email = email ,password = password)
            request.session['customer'] = customer.id
            return redirect('common:home')

        except:

            error_msg = 'email or password is incorrect'



    return render(request,'common/login.html',{'error_msg':error_msg})




def signup(request):

    success_msg =''
    error_msg =''


    if request.method == 'POST':
        cname = request.POST['customer_name']
        cphone = request.POST['phone']
        cemail = request.POST['email']
        cpassword = request.POST['password']

        email_exist = Customer.objects.filter(email = cemail).exists()

        if not email_exist:

            customer = Customer(customer_name = cname ,phone = cphone , email = cemail ,password = cpassword)
            customer.save()
            success_msg = 'you registered successfully'

        else:

            error_msg = 'email is already exist'




    return render(request,'common/signup.html',{'success_message':success_msg,'error_message':error_msg})




    
def change_password(request):

    success_msg = ''
    error_msg = ''


    if request.method == 'POST':

        old_pass = request.POST['old_password']
        new_pass = request.POST['new_password']
        confirm_pass = request.POST['confirm_password']

        if new_pass == confirm_pass :

            if len(new_pass) >= 8 :

                customer = Customer.objects.get(id = request.session['customer'])

                if customer.password == old_pass :

                    # customer.password = new_pass
                    # customer.save()

                    Customer.objects.filter(id = request.session['customer']).update( password = new_pass )

                    success_msg = 'password changed successfully'

                else:
                    error_msg = 'old password is incorrect'

            else:

                error_msg = 'passwords should be 8 characters'


        else:
            error_msg = 'passwords doesn\'t match'
    return render(request,'common/change_password.html',{'success_msg':success_msg,'error_msg':error_msg})




def cart(request):

    cart = Cart.objects.filter(customer = request.session['customer'])
    

    return render(request,'common/cart.html',{'cart_items':cart})


    
def product_detailes(request,pid):

    product = Products.objects.get( id = pid )

    if request.method == 'POST':

        customer = request.session['customer']

        cart = Cart(customer_id =customer ,product_id = pid )
        cart.save()
        return redirect('common:cart')


    
    return render(request,'common/product_detailes.html',{ 'product_detailes':product })