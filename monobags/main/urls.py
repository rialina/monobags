from django.urls import path
from main.views import Home, user_login, user_signup, Cart, user_logout, add_to_cart, remove_from_cart

urlpatterns = [
    path('', Home.as_view(), name='main'),
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('cart/', Cart.as_view(), name='cart'),
    path('logout/', user_logout, name='logout'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/', remove_from_cart, name='remove_from_cart')
]