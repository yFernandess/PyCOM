from django.conf.urls import url

from product import views

urlpatterns = [
    url(r'^$', views.list_products, name='list'),
    url(r'create/?$', views.create_product, name='create'),
    url(r'edit/(?P<id_prod>\d+)', views.edit_product, name='edit'),
    url(r'delete', views.delete_product, name='delete'),
]