from django.shortcuts import render

def create_product(request):
    if request.method == 'GET':
        return render(request, 'produto/create.html')