from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import OrderForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def home_view(request):
    products = Product.objects.all()  
    return render(request, 'home.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})



# افزودن محصول به سبد خرید
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, f'{product.name} به سبد خرید اضافه شد')
    return redirect('cart_view')

# نمایش سبد خرید
@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_amount = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart_view.html', {'cart_items': cart_items, 'total_amount': total_amount})

# حذف یک آیتم از سبد خرید
@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()

    return redirect('cart_view')

# ثبت سفارش
@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items:
        return redirect('home')

    total_amount = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_amount = total_amount
            order.save()
            order.items.set(cart_items)
            cart_items.delete()  # پاک کردن سبد خرید پس از ثبت سفارش
            
            return redirect('home')
            
    else:
        form = OrderForm()

    return render(request, 'checkout.html', {'form': form, 'cart_items': cart_items, 'total_amount': total_amount})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # یا مسیر دلخواه
        else:
            messages.error(request, 'نام کاربری یا رمز عبور نامعتبر است')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'رمزهای عبور مطابقت ندارند')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'نام کاربری از قبل وجود دارد')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'ایمیل قبلاً ثبت شده است')
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            login(request, user)
            return redirect('login')  
    return render(request, 'register.html')



  
    



