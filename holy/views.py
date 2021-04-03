from django.shortcuts import render,get_object_or_404
from django.shortcuts import render,redirect
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate,login,logout
from holy.models import *
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from shop.settings import EMAIL_HOST_USER
# from shop.settings import account_sid,auth_token
# from twilio.rest import Client

def HOME(request):
    cate= CATE_GORY.objects.all()
    news= NEW_ARRIVAL.objects.order_by('id')
    new=news[:6]
    pops=NEW_ARRIVAL.objects.order_by('-id')
    pop=pops[:3]
    d={"new":new,"pop":pop,"cate":cate}
    return render(request,'index.html',d)

def ABT(request):
    cate= CATE_GORY.objects.all()
    return render(request,'about.html',{"cate":cate})

def LOGIN(request):
    cate= CATE_GORY.objects.all()
    if request.method == "POST":
        usernames=request.POST['users']
        password=request.POST['pwds']
        user=auth.authenticate(username=usernames,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('chk')
        else:
            messages.info(request,'invalid credential')
            return redirect('log')
    
    else:
        return render(request,'login.html',{"cate":cate})

def LOGOUT(request):
    #cate= CATE_GORY.objects.all()
    logout(request)
    return redirect('home')

def SHOP(request):
    cate= CATE_GORY.objects.all()
    new=NEW_ARRIVAL.objects.all().order_by('id')
    sort=new.order_by('-price')
    pops=NEW_ARRIVAL.objects.all().order_by('-id')
    pop=pops[:3]
    d={"new":new,"sort":sort,"pop":pop,"cate":cate}
    return render(request,'shop.html',d)

def PRODET(request,pr_id):
    user=request.user
    cate= CATE_GORY.objects.all()
    pot = NEW_ARRIVAL.objects.get(id=pr_id)
    if user.is_authenticated:
        item_in_cart=Cart.objects.filter(Q(product=pot.id) & Q(user=request.user)).exists()
    else:
        return redirect('log')
    d ={"pot":pot,"cate":cate,"items":item_in_cart}
    return render(request,'product_details.html',d)

def CHECK(request):
    cate= CATE_GORY.objects.all()
    user=request.user
    cart=Cart.objects.filter(user=user).exists()
    if request.method == 'POST':
        fn=request.POST['fname']
        ln=request.POST['lname']
        co=request.POST['number']
        em=request.POST['compemailany']
        con=request.POST['country']
        ad1=request.POST['add1']
        ad2=request.POST['add2']
        ci=request.POST['city']
        di=request.POST['dist']
        z=request.POST['zip']
        Customer_detail.objects.create(user=user,first=fn,last=ln,phone=co,email=em,country=con,add1=ad1,add2=ad2,city=ci,dist=di,zipcode=z)
        return redirect('orderd')
    return render(request,'checkout.html',{"cate":cate,"cart":cart})

def Orderd(request):
    user=request.user
    cate= CATE_GORY.objects.all()
    item=Cart.objects.filter(user=user)
    add=Customer_detail.objects.filter(user=user)
    amount=0
    shipping=70
    total_amount=0
    cart_product=[p for p in Cart.objects.all() if p.user == user]
    if cart_product:
        for p in cart_product:
            tempamount=(p.quantity * p.product.price)
            amount += tempamount
            total_amount=amount + shipping
        d={"add":add,"cate":cate,'item':item,'totalamount':total_amount,'amount':amount}
        return render(request,'orderdetail.html',d)
    return render(request,'orderdetail.html',{"cate":cate})

def CONFIRM(request):
    cate= CATE_GORY.objects.all()
    return render(request,'confirmation.html',{"cate":cate})

def CONTACT(request):
    cate= CATE_GORY.objects.all()
    # client = Client(account_sid, auth_token)
    # my_msg = "Congurlations you are successfully registred"
    # message = client.messages.create(to='+917770877002', from_='+15614624702', body=my_msg)
    return render(request,'contact.html',{"cate":cate})



def ELEMENT(request):
    cate=CATE_GORY.objects.all()
    return render(request,'elements.html',{"cate":cate})

def SINGUP(request):
    if request.method == 'POST':
        usernamet=request.POST['usernamesy']
        firstname=request.POST['first_name']
        email=request.POST['email']
        contact=request.POST['contact']
        password=request.POST['password']
        subject = "Congratulation "
        content = "you are succesfully registered in Time"
        msg = EmailMultiAlternatives(subject, f'{content}', EMAIL_HOST_USER, [f'{email}'])
        msg.send()
        # client = Client(account_sid, auth_token)
        # my_msg = "Congurlations you are successfully registred"
        # message = client.messages.create(to=contact, from_='+15614624702', body=my_msg)
        
        

        if User.objects.filter(username=usernamet).exists():
            messages.info(request,'username taken')
            return render(request,'signup.html')
        #elif User.objects.filter(email=email):
           #usages.info(request,'Email taken')
           #return render(request,'signup.html')
        else:
            user = User.objects.create_user(username=usernamet,password=password,email=email,first_name=firstname)
            user.save()
            return redirect('log')
      
    return render(request,'signup.html')

def SHOP1(request,c_id):
    cate= CATE_GORY.objects.all()
    catdata = CATE_GORY.objects.get(id=c_id)
    prod = NEW_ARRIVAL.objects.filter(category=catdata)
    prod1 = prod.order_by('-price')
    prod23 = prod.order_by('-id')
    prod2=prod23[:3]
    d = {"prod":prod,"cat":catdata,"cate":cate,"prod1":prod1,"prod2":prod2}
    return render(request,'shop1.html',d)

# # def search(request):
#     if request.method == 'POST':
#         srch = request.POST['srh']

#         if srch:
#             match = NEW_ARRIVAL.objects.filter(Q(name__icontains=srch))


#             if match:
#                 return render(request,'search.html',{'sr':match})
#         else:
#             return redirect('/home/')
#     return render(request,'index.html')


def Add_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id') 
    product=NEW_ARRIVAL.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('cart')

def Show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cate=CATE_GORY.objects.all()
        add=Customer_detail.objects.filter(user=user).exists()
        cart=Cart.objects.filter(user=user)
        amount=0
        shipping=70
        total_amount=0
        cart_product=[p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity * p.product.price)
                amount += tempamount
                total_amount=amount + shipping
        
            return render(request,'cart.html',{'cate':cate,'carts':cart,'totalamount':total_amount,'amount':amount,"add":add})
        else:
            return render(request,'emptycart.html',{'cate':cate})

def plus_cart(request):
    if request.method =='GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount=0
        shipping=70
        total_amount=0
        cart_product=[p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity * p.product.price)
                amount += tempamount

                data={
                
                  'quantity':c.quantity,
                  'amount':amount,
                  'totalamount':amount + shipping
                }
            return JsonResponse(data)
def minus_cart(request):
    if request.method =='GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount=0
        shipping=70
        total_amount=0
        cart_product=[p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity * p.product.price)
                amount += tempamount
            

                data={
                  'quantity':c.quantity,
                  'amount':amount,
                  'totalamount':amount + shipping
                }
            return JsonResponse(data)


def remove_cart(request):
    if request.method =='GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount=0
        shipping=70
        total_amount=0
        cart_product=[p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity * p.product.price)
                amount += tempamount
            

                data={
                  'amount':amount,
                  'totalamount':amount + shipping
                }
            return JsonResponse(data)

def confirmation(request):
    user=request.user
    cate=CATE_GORY.objects.all()
    custid=request.GET.get('custid')
    customer=Customer_detail.objects.get(id=custid)
    cart=Cart.objects.filter(user=user)
    for c in cart:
        Order_place(user=user,Customer=customer,item=c.product,quantity=c.quantity).save()
        c.delete()
    return render(request,'confirmation1.html',{"cate":cate})

def My_order(request):
    user=request.user
    cate=CATE_GORY.objects.all()
    op=Order_place.objects.filter(user=user).order_by('-id')
    return render(request,"confirmation.html",{"op":op,"cate":cate})


