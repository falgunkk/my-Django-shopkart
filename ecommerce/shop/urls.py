from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url('add_product/', views.add_product, name='add_product'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]