from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('login/', views.login, name="login"),
	path('contact/', views.contact, name="contact"),
	path('category/', views.category, name="category"),
	path('single-product/', views.singleproduct, name="single-product"),
	path('checkout/', views.checkout, name="checkout"),
	path('cart/', views.cart, name="cart"),
	path('confirmation/', views.confirmation, name="confirmation"),
	path('blog/', views.blog, name="blog"),
	path('single-blog/', views.singleblog, name="single-blog"),
	path('tracking/', views.tracking, name="tracking"),
	path('registration/', views.registration, name="registration"),

]