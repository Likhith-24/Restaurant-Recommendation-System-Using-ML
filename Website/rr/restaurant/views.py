
from .restaurant import *

from .models import *



from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required





# Create your views here.
def base(request):
    user = request.user
    context={
        'user' : user,
    }
    return render(request,'base.html',context)

def home(request):
    if request.method == 'POST':
        location=request.POST['Location']
        print(location)
        restaurant = Restaurant.objects.filter(City=location)[:10]
        context= {
            "restaurant" :restaurant ,
            "location" : location
        }
        # Save the form data to the database

        return render(request,'home.html',context)
    else:
        restaurant = Restaurant.objects.all()[:10]
        context= {
            "restaurant" :restaurant 
        }
        return render(request,'home.html',context)
  
    

def baselogin(request):
    return render(request,'baselogin.html')

def recommend(request):
    return render(request, 'recommend.html')


def search(request):
    if 'search' in request.GET:
        q=request.GET['search']
        restaurant= Restaurant.objects.filter(Name__icontains=q).values()
    else:
        restaurant = Restaurant.objects.all()[:10]
    context= {
        "restaurant" :restaurant 
    }
    return render(request,'search.html',context)



def restaurant(request):
    if request.method == 'POST':
        rest_name = request.POST['rest_name']
        restaurant_type = request.POST['restaurant_type']
        restaurant_location = request.POST['restaurant_location']
        restaurant_cost = request.POST['restaurant_cost']

        # Process the data
        # ...
        context={
            'rest_name': rest_name,
            'restaurant_type': restaurant_type,
            'restaurant_location': restaurant_location,
            'restaurant_cost': restaurant_cost,
        }
        # Display the relevant information about the restaurant
        return render(request, 'restaurant.html', context)
    else:
        return render(request, 'restaurant.html')





def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            a="Your password and confirm password are not Same!!"
            context= {'a' : a}
            return render(request,'signup.html',context)
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            a='Username or Password is incorrect!!!'
            context={'a': a}
            return render(request, 'login.html',context)
    return render (request,'login.html')

def LogoutPage(request):
    
    logout(request)
    return redirect('login')
    
def clear(request):
    Order.objects.all().delete()
    return render (request,'cart.html')


def card(request, id):
    # Get the restaurant object with the ID
    restaurants = Restaurant.objects.all()
    filtered_restaurants = restaurants.filter(rest_id=id)
    context=  {'restaurant': filtered_restaurants}
    # Process the restaurant object and return a response
    return render(request, 'restaurant.html', context)


def cart(request,id):

    

    order = Order.objects.create(order_id=id)
    order.save()
    restaurant = Restaurant.objects.filter(rest_id__in=Order.objects.values_list('order_id'))
   
    context= {
         "restaurant" :restaurant,
    }
    return render(request,'cart.html',context)


def carthome(request):
    restaurant = Restaurant.objects.filter(rest_id__in=Order.objects.values_list('order_id'))
   
    context= {
         "restaurant" :restaurant,
    }
    return render(request,'cart.html',context)


def placeorder(request,id):
    if request.method =='POST':

        date= request.POST.get('date')

   
        # Retrieve the current user
        current_user = request.user

        # Use the current user's username
        username = current_user.get_username()
        
        name=Restaurant.objects.filter(rest_id=id).values('Name')
        city=Restaurant.objects.filter(rest_id=id).values('City')
        rating = Restaurant.objects.filter(rest_id=id).values('Ratings')
        cost=Restaurant.objects.filter(rest_id=id).values('Cost')
        order = OrderPlaced.objects.create(order_id=id,user=username,order_date=date,Name=name,City=city,Ratings=rating,Cost=cost)
        order.save()

    #orderplaced=OrderPlaced.objects.filter(user=username)
    restaurant= OrderPlaced.objects.filter(user=username)
   
    context={
        "restaurant" :restaurant,
    }
    return render(request,'placeorderhome.html',context)

def placeorderhome(request):
    # Retrieve the current user
    current_user = request.user

    # Use the current user's username
    username = current_user.get_username()
    #orderplaced=OrderPlaced.objects.filter(user=username)
    
    
    #order= OrderPlaced.objects.filter(user=username,order_id=restaurant.objects.filter(rest_id))
    restaurant= OrderPlaced.objects.filter(user=username)
    context={
        "restaurant" :restaurant,
        
    }
    return render(request,'placeorderhome.html',context)


def removeorder(request,id):
    OrderPlaced.objects.filter(order_id=id).delete()
    current_user = request.user

    # Use the current user's username
    username = current_user.get_username()
    #orderplaced=OrderPlaced.objects.filter(user=username)
    restaurant= Restaurant.objects.filter(rest_id__in=OrderPlaced.objects.filter(user=username).values_list('order_id'))
    context={
        "restaurant" :restaurant,
    }
    return render(request,'placeorderhome.html',context)


