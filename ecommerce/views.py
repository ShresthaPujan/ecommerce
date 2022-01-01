from django.shortcuts import render
from django.http import HttpResponseBadRequest
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_availabe= True)
    return render(request,'home.html',{'products':products})