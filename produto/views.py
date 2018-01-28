from django.shortcuts import render

from produto.forms import ProductModelForm

def create_product(request):
    form = ProductModelForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return render(request, "Redirect para lista de produtos")

    return render(request, 'produto/create.html', {"form": form})