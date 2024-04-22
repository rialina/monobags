from main.utils import HomeMixin, CartMixin
from django.shortcuts import render
from main.forms import SignupForm, LoginForm
from django.shortcuts import redirect
from main.models import Product
from django.contrib.auth import authenticate, login, logout

class Home(HomeMixin):
    template_name = 'main/main.html'

class Cart(CartMixin):
    template_name = 'main/cart.html'

def add_to_cart(request):
    if request.method == 'POST' and request.user.is_authenticated:
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        product.users.add(request.user)
        return redirect('main')
    else:
        return redirect('login')
    
def remove_from_cart(request):
    if request.method == 'POST' and request.user.is_authenticated:
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        product.users.remove(request.user)
        return redirect('cart')
    else:
        return redirect('login')

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'main/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('main')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')