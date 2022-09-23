from django.urls import path
# from . import views
# from .views import index,about, contact
# from .views import contact, index
from .views import *


urlpatterns = [
    path('', index, name ='index'),
    path('contact', contact, name='contact'),
    path('all_food', all_food, name='all_food'),
    path('category', category, name='category'),
    path('signin', signin, name='signin'),
    path('signup', signup, name='signup'),
    path('signout', signout, name='signout'),
    path('category/<str:id>', single_category, name='single_category'),
    path('detail/<str:id>', detail, name='detail'),
    path('profile', profile, name='profile'),
    path('profile_update', profile_update, name='profile_update'),
    path('passwordupdate', passwordupdate, name='passwordupdate'),
    path('addtocart', ordermeal, name='addtocart'),
    path('mycart', mycart, name='mycart'),
    path('deletemeal', deletemeal, name='deletemeal'),
    path('deleteallmeal', deleteallmeal, name='deleteallmeal'),
    path('checkout', checkout, name='checkout'),
    path('payment', payment, name='payment'),
    path('decrease', decrease, name='decrease'),
    path('increase', increase, name='increase'),
    path('completed', completed, name='completed'),

]

    
    
    
    
    

