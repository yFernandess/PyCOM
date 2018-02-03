# coding: utf-8

from django.shortcuts import render, redirect, get_object_or_404

from product.forms import ProductModelForm
from product.models import Product


def list_products(request):
    products = Product.objects.all().order_by("name", "bar_code")

    return render(request, "product/list.html", {"products": products})


def create_product(request):
    form = ProductModelForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("product:list")

    return render(request, 'product/form.html', {"form": form})

def edit_product(request, id_prod):
    product = get_object_or_404(Product, pk=id_prod)
    form = ProductModelForm(request.POST or None, instance=product)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("product:list")

    return render(request, 'product/form.html', {"form": form})


def delete_product(request):
    id_prod = request.POST.get("id_prod")

    if id_prod:
        Product.objects.filter(pk=id_prod).delete()

    return redirect("product:list")



# API

def api_product(request):
    # POST - > create prod
    # GET -> retornar lista de product
    # put -> retornar 405
    # delete -> 405
    pass

def api_product_id(request, id_prod):
    # get -> product com o id
    # post -> atualizar product
    # put -> atualizar product
    # deletar -> product

    # se nao encontrou -> 404
    pass