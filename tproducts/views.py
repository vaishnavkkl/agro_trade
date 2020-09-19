from django.shortcuts import render
from django.http import HttpResponse
from .models import TProduct


def index(request):
    products = TProduct.objects.all()
    return render(request ,'index.html',{'products':products})

