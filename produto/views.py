from django.shortcuts import render, redirect, get_object_or_404

from produto.forms import ProductModelForm
from produto.models import Produto


def list_products(request):
    products = Produto.objects.all().order_by("name", "bar_code")

    return render(request, "produto/list.html", {"products": products})


def create_product(request):
    form = ProductModelForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("product:list")

    return render(request, 'produto/form.html', {"form": form})

def edit_product(request, id_prod):
    produto = get_object_or_404(Produto, pk=id_prod)
    form = ProductModelForm(request.POST or None, instance=produto)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("product:list")

    return render(request, 'produto/form.html', {"form": form})


def delete_product(request):
    id_prod = request.POST.get("id_prod")

    if id_prod:
        Produto.objects.filter(pk=id_prod).delete()

    return redirect("product:list")



# API

def api_product(request):
    # POST - > create prod
    # GET -> retornar lista de produto
    # put -> retornar 405
    # delete -> 405
    pass

def api_product_id(request, id_prod):
    # get -> produto com o id
    # post -> atualizar produto
    # put -> atualizar produto
    # deletar -> produto

    # se não encontrou -> 404
    pass
