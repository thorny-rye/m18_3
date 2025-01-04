from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def main_page(request):
    return render(request, "third_task/platform.html")

def catalog(request):
    return render(request, 'third_task/games.html', context=games)

def purchases(request):
    return render(request, 'third_task/cart.html')