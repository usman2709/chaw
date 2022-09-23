from email.mime import image
from importlib.abc import ExecutionLoader
import json
from multiprocessing import context
import uuid
from unicodedata import name
from webbrowser import get

import requests
import json

from django.core.mail import EmailMessage
from django.conf import settings

# from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# from techbro.models import Category, Dish, Showcase
from dashboard.models import *
from techbro.models import *
from cart.models import *
from techbro.forms import SignupForm
from dashboard.forms import ProfileUpdateForm
# from techbro.models import *  - this is used for universal selector, this import all models


# Create your views here.
# def index(request):
#     return HttpResponse('TechBros are here to sky high')
#     # return render(request, 'index.html')
# def about(request):
#     return HttpResponse('TechBros are here to sky high')
#     # return render(request, 'index.html')
# def contact(request):
#     return HttpResponse('TechBros are here to sky high')
#     # return render(request, 'index.html')

def index(request):
    #query the database to pull objects out
    categories = Category.objects.all()[:6]
    specials = Dish.objects.filter(special=True)
    slide1 = Showcase.objects.get(pk=1)
    slide2 = Showcase.objects.get(pk=2)
    slide3 = Showcase.objects.get(pk=3)

    

    context ={
        'categories':categories,
        'specials':specials,
        'slide1': slide1,
        'slide2': slide2,
        'slide3': slide3,
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')



def all_food(request):
    all_meals = Dish.objects.all()
    categories = Category.objects.all()[:6]
    slide1 = Showcase.objects.get(pk=1)
    slide2 = Showcase.objects.get(pk=2)
    slide3 = Showcase.objects.get(pk=3)

    context ={
        'all_meals':all_meals,
        'categories':categories,
        'slide1': slide1,
        'slide2': slide2,
        'slide3': slide3,
    }
    
    return render(request, 'all_food.html', context)

def category(request):
    categories = Category.objects.all()
    slide1 = Showcase.objects.get(pk=1)
    slide2 = Showcase.objects.get(pk=2)
    slide3 = Showcase.objects.get(pk=3)
    context ={
        'categories':categories,
        'slide1': slide1,
        'slide2': slide2,
        'slide3': slide3,

    }


    return render(request, 'category.html', context)

def single_category(request, id):
      categories = Category.objects.all()
      specials = Dish.objects.filter(special=True)
      single_category = Dish.objects.filter(category_id = id)
      slide1 = Showcase.objects.get(pk=1)
      slide2 = Showcase.objects.get(pk=2)
      slide3 = Showcase.objects.get(pk=3)
      cat_title = Category.objects.get(pk=id)


      context ={
        'categories':categories,
        'specials':specials,
        'singcat': single_category,
        'slide1': slide1,
        'slide2': slide2,
        'slide3': slide3,
        'cat_title': cat_title
      
    }

      return render(request,'single_category.html', context )

def detail(request, id):
    categories = Category.objects.all()
    specials = Dish.objects.filter(special=True)
    slide1 = Showcase.objects.get(pk=1)
    slide2 = Showcase.objects.get(pk=2)
    slide3 = Showcase.objects.get(pk=3)
    detail = Dish.objects.get(pk=id)
    
    context ={
        'categories':categories,
        'specials':specials,
        'slide1': slide1,
        'slide2': slide2,
        'slide3': slide3,
        'detail': detail,
      
    }

    return render(request, 'detail.html', context)

def signin(request):
    
    if request.method == "POST":
      myusername = request.POST['username']
      mypassword = request.POST['password']
      user = authenticate(request, username= myusername, password = mypassword,)
      
      if user:
         login(request, user)
         messages.success(request, f'Dear {user.username}, your signin is suceessfully, welcome!')
         return redirect('index')
      else:
          messages.warning(request, f'Username /Password is incorrect')
          return redirect('signin')

    return render(request, 'signin.html',)

def signout(request):
    logout(request)
    messages.success(request, 'You have now signed out successfully')
    return render(request, 'signin.html',)

def signup(request):
    # make a get request to pull out and display the SignupForm
    form = SignupForm() #Instantiate the SignupForm for GET request
    if request.method  == 'POST': 
        phone = request.POST['phone']
        form = SignupForm(request.POST)#Instantiate the SignupForm for POST request
        if form.is_valid():#test form for virus free, and declare valid
            form.save()#save incoming data
            userform = form.save()
            newuser = Profile(user= userform)
            newuser.first_name = userform.first_name
            newuser.last_name = userform.last_name
            newuser.email = userform.email
            newuser.phone = phone
            newuser.save()
            messages.success(request, 'You have now signed up successfully')# sends success message to your user
            login(request, userform)
            return redirect('index')# redirect the user to any page of your choice after filling form
        else:
            messages.error(request, form.errors)

            return redirect('signup')# if error redirect user to signup attempt
  

    return render(request, 'signup.html')



#dashboard configuration
def profile(request):
    
    profile_data = Profile.objects.get(user__username = request.user.username)


    context ={

        'profile_data': profile_data

    }

    return render(request, 'dash.html', context)
@login_required(login_url='signin')
def profile_update(request):
    form = ProfileUpdateForm(instance=request.user.profile)
    profile_data = Profile.objects.filter(user__username=request.user.username)
    if request.method  == 'POST': 
        form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)#Instantiate the SignupForm for POST request
        if form.is_valid():#test form for virus free, and declare valid
            form.save()#save incoming data
            messages.success(request, 'Update successful')# sends success message to your user
            return redirect('profile')# redirect the user to any page of your choice after filling form
        else:
            messages.error(request, form.errors)# send out error message
            return redirect('profile_update')# if error redirect user to signup attempt
    context = {
       'form': form,
       'profile_data':profile_data,
    }

    return render(request, 'profile_update.html', context)


def passwordupdate(request):
     profile_data = Profile.objects.get(user__username = request.user.username)
     form = PasswordChangeForm(request.user)
     if request.method == 'POST':
        form =PasswordChangeForm(request.user, request.POST)
        if form.is_valid():#test form for virus free, and declare valid
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request, 'Password Update successful')# sends success message to your user'S PASS
            return redirect('profile')# redirect the user to any page of your choice after filling form
        else:
            messages.error(request, form.errors)# send out error message
            return redirect('passwordupdate')# if error redirect user to signup attempt


     context ={
     'profile_data': profile_data,
     'form': form,
       }
    


     return render(request, 'profilepassword.html', context)



def ordermeal(request):
    profile_data = Profile.objects.get(user__username = request.user.username)
    cart_no = profile_data.id
    if request.method == 'POST':
        quantityselected = int(request.POST['mealquantity'])
        meal = request.POST['mealid']
        mealselected = Dish.objects.get(pk=meal)
        cart = Shopcart.objects.filter(user__username = request.user.username, paid =False)
        if cart:
            basket = Shopcart.objects.filter(dish = mealselected.id, user__username = request.user.username,paid =False).first() 
            if basket:
                basket.quantity += quantityselected
                basket.amount = basket.quantity * basket.c_price
                basket.save()
                messages.success(request,'Your meal is being proccessed')
                return redirect('all_food')
            else:
                neworder = Shopcart()
                neworder.user = request.user
                neworder.dish = mealselected
                neworder.c_name = mealselected.name
                neworder.c_item = 1
                neworder.quantity =quantityselected
                neworder.c_price = mealselected.price
                neworder.amount = mealselected.price * quantityselected
                neworder.cart_code = cart_no
                neworder.paid = False
                neworder.save()
                messages.success(request, 'Meal added to basket')
                return redirect('all_food')
        else:
            newitem =Shopcart()
            newitem.user = request.user
            newitem.dish = mealselected
            newitem.c_name = mealselected.name
            newitem.c_item = 1
            newitem.quantity =quantityselected
            newitem.c_price = mealselected.price
            newitem.amount = mealselected.price * quantityselected
            newitem.cart_code = cart_no
            newitem.paid = False
            newitem.save()
            messages.success(request, 'Meal added to basket')
    return redirect('all_food')

#@login_required(login_url='signin')


def mycart(request):
    profile = Profile.objects.get(user__username = request.user.username)

    shopcart = Shopcart.objects.filter(user__username = request.user.username, paid = False)
    subtotal = 0
    vat = 0
    total = 0
   

    for item in shopcart:
        subtotal += item.amount
        vat = 0.075 * subtotal
        total = vat + subtotal
       

    context={
     'profile' : profile,
     'shopcart' :shopcart,
     'subtotal' : subtotal,
     'vat': vat,
     'total': total,
    
     }


    return render ( request, 'mycart.html', context)


def deletemeal(request):
    if request.method == 'POST':
        meal = request.POST['dishid']
        deletedish = Shopcart.objects.get(pk=meal)
        deletedish.delete()
        messages.success(request, 'Meal deleted successfully')
    return redirect('mycart')


def deleteallmeal(request):
    if request.method == 'POST':
        meal = request.POST['alldishid']
        deletealldish = Shopcart.objects.filter(user__username = request.user.username)
        deletealldish.delete()
        messages.success(request, ' All Meal deleted successfully')
    return redirect('mycart')


def decrease(request):
     if request.method == 'POST':
        itemquantity = int(request.POST['decrease'])
        cartitem = request.POST['itemid']
        decreasecart = Shopcart.objects.get(pk = cartitem)
        decreasecart.quantity  -= itemquantity
        decreasecart.amount  = decreasecart.c_price * decreasecart.quantity
        decreasecart.save()
        messages.success(request, 'Quantity decreased.')

     return redirect('mycart')

def increase(request):
    if request.method == 'POST':
        itemquantity = int(request.POST['increase'])
        cartitem = request.POST['itemid']
        increasecart = Shopcart.objects.get(pk = cartitem)
        increasecart.quantity  += itemquantity
        increasecart.amount  = increasecart.c_price * increasecart.quantity
        increasecart.save()
        messages.success(request, 'Quantity increase.')
    return redirect('mycart')

@login_required(login_url='signin')
def checkout(request):
    profile = Profile.objects.get(user__username = request.user.username)

    shopcart = Shopcart.objects.filter(user__username = request.user.username, paid = False)
    subtotal = 0
    vat = 0
    total = 0
   

    for item in shopcart:
        subtotal += item.amount

        vat = 0.075 * subtotal
        total = vat + subtotal
       

    context={
     'profile' : profile,
     'shopcart' :shopcart,
     'subtotal' : subtotal,
     'vat': vat,
     'total': total,
    
     }


    return render ( request, 'checkout.html', context)




#
def payment(request):
    if request.method =='POST':
        api_key = 'sk_test_b2a5b077239633bf9c06ca34bf16b0b49a1071a0'
        curl = 'https://api.paystack.co/transaction/initialize'
        cburl = 'http://3.83.92.98/completed'
        ref_code = str(uuid.uuid4())
        user = User.objects.get(username= request.user.username)
        email =user.email
        profile = Profile.objects.get(user__username= request.user.username)
        cart_code = profile.id
        total = float(request.POST['total']) * 100
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        new_email = request.POST['email']
    

        headers = {'Authorization': f'Bearer {api_key}'}
        data = {'reference': ref_code , 'amount': int(total) , 'order_number': cart_code , 'email': email , 'callback_url': cburl , 'currency': 'NGN'}

        try: # make call to paystack
            r = requests.post(curl, headers=headers, json=data)# pip install requests
        except Exception:
            messages.error(request, 'Network Busy try again')
        else:
            transback = json.loads(r.text)#import json , import requests
            rurl =transback['data']['authorization_url']

            account = Payment()
            account.user = user
            account.first_name =fname
            account.last_name = lname
            account.phone_no = phone
            account.address = address
            account.city = city
            account.total = total/100
            account.cart_code = cart_code
            account.pay_code = ref_code
            account.paid = True
            account.save()

            email = EmailMessage(
                'Order Confirmation',#Title
                f'Dear {fname}, your order is confrimed! \n Your delivery is in one hour. Thank you ',#content
                settings.EMAIL_HOST_USER,#company email
                [new_email])#client email
                
            email.fail_silently=True
            email.send()

            return redirect(rurl)

    return redirect('checkout')

def completed(request):
    profile = Profile.objects.get(user__username= request.user.username)
    cart = Shopcart.objects.filter(user__username= request.user.username, paid = False)
    for item in cart:
        item.paid = True
        item.save()

        stock = Dish.objects.get(pk = item.dish.id)
        stock.max -= item.quantity 
        stock.save()
    context = {
        'profile' : profile
    }

    return render(request,'completed.html', context )
