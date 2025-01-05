from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def main_page(request):
    mn_page = "Главная страница"
    context = {'title': mn_page}
    return render(request, "third_task/platform.html", context)

def catalog(request):
    title = "Игры"
    context = {"title2": title,
               'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"]}
    return render(request, 'third_task/games.html', context)

def purchases(request):
    cart = 'Корзина'
    context = {"cart": cart}
    return render(request, 'third_task/cart.html', context)