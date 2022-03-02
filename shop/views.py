from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse ('About page in shop')

def contact(request):
    return HttpResponse ('Contact page in shop')

def tracker(request):
    return HttpResponse ('Tracker page in shop')

def search(request):
    return HttpResponse ('Search page in shop')

def productView(request):
    return HttpResponse ('Product View page in shop')

def checkout(request):
    return HttpResponse ('Checkout page in shop')