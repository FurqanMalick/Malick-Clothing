from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='shop home'),
    path('about', views.about, name='shop about'),
    path('contact', views.contact, name='shop contact'),
    path('tracker', views.tracker, name='shop tracker'),
    path('search', views.search, name='shop search'),
    path('productView', views.productView, name='shop productView'),
    path('checkout', views.checkout, name='shop checkout'),
]
