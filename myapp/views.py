from django.shortcuts import render, redirect

from django.http import HttpResponse
from . models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator

# Create your views here.

def index(request):
	return HttpResponse("Hello world")

# Function based 
def products(request):
	page_obj = products = Product.objects.all()

	product_name = request.GET.get('product_name')
	if product_name != '' and product_name is not None:
		page_obj = products.filter(name__icontains = product_name)
	paginator = Paginator(page_obj, 3)
	page_num = request.GET.get('page')
	page_obj = paginator.get_page(page_num)

	context = {
		'page_obj':page_obj
	}
	return render(request, 'myapp/index.html', context)

# Class based view
class ListOfProducts(ListView):
	model = Product
	template_name = 'myapp/index.html'
	context_object_name = 'products'
	paginate_by = 3



# function based
def detailed(request, id):
	product = Product.objects.get(id=id)

	context = {
		'product':product
	}
	return render(request, 'myapp/detail.html', context)

class ProductDetailView(DetailView):
	model = Product
	template_name = "myapp/detail.html"
	context_object_name = 'product'



# function based 
@login_required
def addprod(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		price = request.POST.get('price')
		desc = request.POST.get('description')
		image = request.FILES['upload']
		seller_name = request.user

		product = Product(name=name, price=price, description=desc, image=image, seller_name=seller_name)
		product.save()

	return render(request, 'myapp/addproduct.html')


#class based
class AddProduct(CreateView):
	model = Product
	fields = ['name', 'price', 'description', 'image', 'seller_name']



#function based
def update_product(request, id):
	product = Product.objects.get(id=id)
	if request.method == 'POST':
		product.name = request.POST.get('name')
		product.price = request.POST.get('price')
		product.description = request.POST.get('description')
		print(request.FILES['upload'])
		if request.FILES['upload'] == '':
			product.image = request.FILES['upload']
		product.save()

		return redirect('/myapp/products')

	
	context = {
		'product':product
	}
	return render(request, 'myapp/updateproduct.html', context)


#class based
class UpdateProduct(UpdateView):
	model = Product
	fields = ['name', 'price', 'description', 'image', 'seller_name']
	template_name_suffix = '_update_form'


# funtion based
def delete_product(request, id):
	product = Product.objects.get(id=id)
	context = {
		'product':product,
	}
	if request.method == 'POST':
		product.delete()
		return  redirect('/myapp/products')
	
	return render(request, 'myapp/delete.html', context)
	

#class based
class DeleteProduct(DeleteView):
	model = Product
	success_url = reverse_lazy("myapp:products")



def my_listings(request):
	products = Product.objects.filter(seller_name = request.user)

	context = {
		"products":products,
	}

	return render(request, 'myapp/mylistings.html', context=context)