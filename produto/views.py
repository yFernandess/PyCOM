import json

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
@csrf_exempt
def api_product(request):
    # put -> retornar 405
    # delete -> 405
    if request.method in ["PUT", "DELETE"]:
        resp = HttpResponse()
        resp.status_code = 405
        return resp

    # GET -> retornar lista de produto
    if request.method == "GET":
        products = []
        for produto in Produto.objects.all().order_by("name", "bar_code"):
            products.append(produto.to_dict())

        return HttpResponse(json.dumps(products))

    # POST - > create prod
    if request.method == "POST":
        input_data = json.loads(request.body.decode("utf-8")) or None
        form = ProductModelForm(input_data)

        if form.is_valid():
            product = form.save()
            resp = HttpResponse(json.dumps({"prod_id": product.pk}))
            resp.status_code = 201

            return resp
        else:
            resp = HttpResponse(json.dumps(form.errors))
            resp.status_code = 400

            return resp

@csrf_exempt
def api_product_id(request, id_prod):
    # se não encontrou -> 404
    product = get_object_or_404(Produto, pk=id_prod)

    # get -> produto com o id
    if request.method == "GET":
        return HttpResponse(json.dumps(product.to_dict()))

    # post -> atualizar produto
    # put -> atualizar produto
    if request.method in ["POST", "PUT"]:
        input_data = json.loads(request.body.decode("utf-8")) or None
        form = ProductModelForm(input_data, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({"prod_id": product.pk}))
        else:
            resp = HttpResponse(json.dumps(form.errors))
            resp.status_code = 400
            return resp
    # delete -> produto
    if request.method == "DELETE":
        product.delete()
        return HttpResponse()
