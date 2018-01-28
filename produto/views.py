from django.shortcuts import render, redirect

from produto.forms import ProductModelForm
from produto.models import Produto

def list_products(request):
    products = Produto.objects.all()

    return render(request, "produto/list.html", {"products": products})


def create_product(request):
    form = ProductModelForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("product:list")

    return render(request, 'produto/create.html', {"form": form})