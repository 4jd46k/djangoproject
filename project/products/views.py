from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth.password_validation import validate_password
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    if 'usr' in request.session:
        products = Product.objects.all()
        return render(request, 'index.html', {'products': products})
    else:
        return redirect(loginn)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)

def loginn(request):
    if 'usr' in request.session:
        return redirect(index)
    
    if request.method == 'POST':
        uname = request.POST['usr']
        pword = request.POST['pas']
        print(uname, pword)
        user = authenticate(request, username=uname, password=pword)
        
        if user is not None:
            request.session['usr'] = uname
            return redirect(index)
    
    return render(request, 'login.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)

def lout(request):
    logout(request)
    return redirect(loginn)

def validate_user_password(password):
    try:
        validate_password(password)
        return True  
    except Exception as e:
        return False  
@cache_control(no_cache=True, must_revalidate=True, no_store=True)

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        Cpassword = request.POST['password1']
        
        if password == Cpassword and validate_user_password(password):
            print(username, password, Cpassword)
            myuser = User.objects.create_user(username, email, password)
            myuser.save()
            return redirect(loginn)
        else:
            return HttpResponse('<br> <br> <p style="text-align: center;"> <b> PASSWORD MUST BE </b> <br>- <br> ~ Both Passwords must be same <br>  <br> ~ Minimum length of 8 characters <br> <br> ~ Must not be a common password <br> <br> ~ Must contain at least one numeric digit <br> <br> ~ Must contain at least one Capital letter <br> <br> ~ Must contain at least one special character (!,@,%) <br> <br> ~ Must not be a common password <br> <br> ~ Must contain at least one numeric digit <br> <br> ~ Must contain at least one Capital letter </p>')
    
    return render(request, 'signup.html')

def policy(request):
    return HttpResponse('<h5>Terms & Conditions</h5>')
