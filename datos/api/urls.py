from django.urls import path
from . import views



urlpatterns = [
    path('register',views.register),
    path('login', views.login),
    # path('products/', ProductListView.as_view(), name='product_list'),
    # path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    # path('orders/', OrderListView.as_view(), name='order_list'),
    # path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
]


