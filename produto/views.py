from django.shortcuts import render

from produto.forms import ProductModelForm

def create_product(request):
    if request.method == 'GET':
        context = {'form': ProductModelForm()}
        return render(request, 'produto/create.html', context)