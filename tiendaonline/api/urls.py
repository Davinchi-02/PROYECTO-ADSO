from django.urls import path
from .views import RegisterUser, LoginView, ProductListView, OrderCreateView, OrderListView

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('orders/', OrderCreateView.as_view(), name='order-create'),
    path('orders/my/', OrderListView.as_view(), name='order-list'),
]
