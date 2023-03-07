from django.shortcuts import render
from django.views.generic import ListView

from app1.models import Item


class HomePageView(ListView):
    items = Item.objects.all()
    model = Item
    template_name = 'home_page.html'
    context_object_name = 'items'
