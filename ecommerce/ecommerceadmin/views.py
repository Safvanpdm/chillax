from django.shortcuts import render,redirect
from .models import Admin,Products
from common.models import Customer

# Create your views here.

def index(request):

    admin = Admin.objects.filter(id= request.session['admin']).values('admin_name')
    admin_name = admin[0]['admin_name']

    return render(request,'ecommerceadmin/index.html',{'name':admin_name})
def login(request):

    error_msg = ''

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        try:
            admin = Admin.objects.get(email = email ,password = password)
            request.session['admin'] = admin.id
            return redirect('ecommerceadmin:adminhome')

        except:

            error_msg = 'email or password is incorrect'

    return render(request,'ecommerceadmin/login.html',{'error':error_msg})

def add_product(request):

    success_msg = ''
    error_msg = ''

    if request.method == 'POST':

        product_name = request.POST['product_name']
        description = request.POST['description']
        price = request.POST['product_price']
        stock = request.POST['product_stock']
        code = request.POST['product_code']
        product_image = request.FILES['product_image']
        

        product_exist = Products.objects.filter(code = code ,admin = request.session['admin']).exists()  #it returns false or true

        if not product_exist:            

            product = Products(product_name = product_name , description = description , price = price , stock = stock , image = product_image , code = code , admin_id = request.session['admin'])
            product.save()
            success_msg ='product added successfully'

        else:

            error_msg = 'product is already added'

    return render(request,'ecommerceadmin/add_product.html',{'success':success_msg,'error':error_msg})

def update_stock(request):
    return render(request,('ecommerceadmin/update_stock.html'))

def catalogue(request):

    products = Products.objects.filter(admin = request.session['admin'])
    
    return render(request,'ecommerceadmin/catalogue.html',{'products':products})

def order_history(request):
    return render(request,('ecommerceadmin/order_history.html'))

def change_password(request):

    error_msg = ''
    success_msg = ''

    if request.method == 'POST':

        old_pass = request.POST['old_password']
        new_pass = request.POST['new_password']
        confirm_pass = request.POST['confirm_password']

        if new_pass == confirm_pass :

            if len(new_pass) >= 8 :

                customer = Admin.objects.get(id = request.session['admin'])

                if customer.password == old_pass :

                    # customer.password = new_pass
                    # customer.save()

                    Admin.objects.filter(id = request.session['admin']).update( password = new_pass )
                    success_msg = 'password changed successfully'

                else:
                    error_msg = 'old password is incorrect'

            else:

                error_msg = 'passwords should be 8 characters'


        else:
            error_msg = 'passwords doesn\'t match'
    return render(request,'ecommerceadmin/change_password.html',{'success':success_msg,'error':error_msg})

def customers(request):

    customer = Customer.objects.all()
    return render(request,'ecommerceadmin/customers.html',{'customer_list':customer})

def signup(request):

    success_msg =''
    error_msg =''


    if request.method == 'POST':
        aname = request.POST['admin_name']
        aphone = request.POST['phone']
        aemail = request.POST['email']
        apassword = request.POST['password']

        email_exist = Admin.objects.filter(email = aemail).exists()

        if not email_exist:

            admin = Admin(admin_name = aname ,phone = aphone , email = aemail ,password = apassword)
            admin.save()
            success_msg = 'you registered successfully'

        else:

            error_msg = 'email is already exist'

    return render(request,'ecommerceadmin/signup.html',{'error':error_msg,'success':success_msg})

def logout(request):
    del request.session['admin']
    request.session.flush()
    return redirect('ecommerceadmin:login')