from django.shortcuts import render

def store(request):
	context = {}
	return render(request, 'store/store.html', context)

def cart(request):
	context = {}
	return render(request, 'store/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)

def login(request):
	context = {}
	return render(request, 'store/login.html', context)

def contact(request):
	context = {}
	return render(request, 'store/contact.html', context)

def category(request):
	context = {}
	return render(request, 'store/category.html', context)
	
def singleproduct(request):
	context = {}
	return render(request, 'store/single-product.html', context)

def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)

def cart(request):
	context = {}
	return render(request, 'store/cart.html', context)

def confirmation(request):
	context = {}
	return render(request, 'store/confirmation.html', context)	

def blog(request):
	context = {}
	return render(request, 'store/blog.html', context)
	
def singleblog(request):
	context = {}
	return render(request, 'store/single-blog.html', context)
	
def tracking(request):
	context = {}
	return render(request, 'store/tracking.html', context)

def registration(request):
	context = {}
	return render(request, 'store/registration.html', context)

	