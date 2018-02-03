from django.conf.urls import url

from product import views

urlpatterns = [
    url(r'^/?$', views.api_product, name='product_api'),
    url(r'(?P<id_prod>\d+)/?$', views.api_product_id, name="product_api_id")
]