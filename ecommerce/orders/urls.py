from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^order_details/$',views.order_details, name='order_details'),
    url(r'^test/$',views.test, name='test')
]