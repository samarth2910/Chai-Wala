from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.all_chai, name="all_chai"),
    path('<int:chai_id>/', views.chai_detail, name="chai_detail"),
    path('home/', views.chai_home, name="chai_home"),
    path('cart/', views.view_cart, name='view_cart'),
    path('login/', auth_views.LoginView.as_view(template_name='Chai/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('chai_home')), name='logout'),
    path('signup/', views.signup_view, name='signup'),
        path('cart/', views.cart_view, name='cart'),  # For live reloading during development
path('update-cart/<int:chai_id>/<str:action>/', views.update_cart, name='update_cart'),
    path('add-to-cart/<int:chai_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
path('orders/', views.my_orders, name='my_orders'),
path('remove-from-cart/<int:chai_id>/', views.remove_from_cart, name='remove_from_cart'),
path('api/products/', views.api_chai_list, name='api_chai_list'),
path('api/orders/', views.api_my_orders, name='api_my_orders'),
]