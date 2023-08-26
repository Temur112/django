from django.contrib import admin
from django.urls import path

from . import views

app_name='myapp'
urlpatterns = [
    path('', views.index),
    path('products/', views.products, name='products'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='detailed_page'),
    path('products/add/', views.AddProduct.as_view(), name='add_product'),
    path('products/update/<int:pk>', views.UpdateProduct.as_view(), name='update_product'),
    path('products/delete/<int:pk>', views.DeleteProduct.as_view(), name='delete_product'),
    path('products/mylistings', views.my_listings, name='mylistings')
]