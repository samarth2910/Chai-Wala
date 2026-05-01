from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Chai
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ChaiSerializer, OrderSerializer
    
    

# Create your views here.
def all_chai(request):
    # This view will render a template that lists all chai items
    chai_info= Chai.objects.all()  # Fetch all Chai objects from the database
    return render(request, 'Chai/all_chai.html', {'chais': chai_info})

def chai_detail(request, chai_id):
    # This view will render a template that shows details of a specific chai item
    chai_item = get_object_or_404(Chai,pk=chai_id)  # Fetch a specific Chai object by its ID
    return render(request, 'Chai/chai_detail.html', {'chai': chai_item})

def chai_home(request):
    print("🟢 User redirected to home after logout")
    chai_info = Chai.objects.all()  # Fetch all Chai objects from the database
    return render(request, 'Chai/chai_home.html', {'chais': chai_info})

def view_cart(request):
    return HttpResponse("Cart page coming soon!")

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Signup successful! You can now log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'Chai/signup.html', {'form': form})

def add_to_cart(request, chai_id):
    cart = request.session.get('cart', {})
    chai = get_object_or_404(Chai, pk=chai_id)
    
    str_id = str(chai_id)
    if str_id in cart:
        cart[str_id]['quantity'] += 1
    else:
        cart[str_id] = {
            'name': chai.name,
            'price': float(chai.price),
            'quantity': 1,
        }
    
    request.session['cart'] = cart
    messages.success(request, f"{chai.name} added to cart!")
    return redirect('view_cart')


def view_cart(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'Chai/cart.html', {'cart': cart, 'total': total})

def cart_view(request):
    cart = [
        {"name": "Masala Tea", "price": 500},
        {"name": "Green Tea", "price": 300},
    ]
    return render(request, 'website/cart.html', {'cart_items': cart})

def remove_from_cart(request, chai_id):
    cart = request.session.get('cart', {})
    cart.pop(str(chai_id), None)
    request.session['cart'] = cart
    return redirect('view_cart')

def update_cart(request, chai_id, action):
    cart = request.session.get('cart', {})
    str_id = str(chai_id)
    
    if str_id in cart:
        if action == 'increase':
            cart[str_id]['quantity'] += 1
        elif action == 'decrease':
            if cart[str_id]['quantity'] > 1:
                cart[str_id]['quantity'] -= 1
            else:
                cart.pop(str_id)  # Remove if quantity hits 0
    
    request.session['cart'] = cart
    return redirect('view_cart')

from .models import Chai, Order, OrderItem
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')   # redirects to login if not signed in
def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        messages.error(request, "Your cart is empty!")
        return redirect('view_cart')

    # Calculate total
    total = sum(float(item['price']) * item['quantity'] for item in cart.values())

    # Create the Order
    order = Order.objects.create(user=request.user, total=total)

    # Create each OrderItem
    for item in cart.values():
        OrderItem.objects.create(
            order=order,
            chai_name=item['name'],
            price=item['price'],
            quantity=item['quantity']
        )

    # Clear the cart
    request.session['cart'] = {}
    messages.success(request, f"Order #{order.id} placed successfully! 🎉")
    return redirect('my_orders')


@login_required(login_url='login')
@login_required(login_url='login')
def my_orders(request):
    return render(request, 'Chai/react_orders.html')

@api_view(['GET'])
def api_chai_list(request):
    # Returns all teas as JSON
    chais = Chai.objects.all()
    return Response(ChaiSerializer(chais, many=True).data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_my_orders(request):
    # Returns logged-in user's orders as JSON
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return Response(OrderSerializer(orders, many=True).data)