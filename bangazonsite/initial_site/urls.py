from django.conf.urls import url
from . import views


# Products View / Creation
urlpatterns += [
    url(r'^products/', views.get_product_types, name='products'),
    url(r'^products_of_type/(?P<pk>\d+)/', views.get_products_of_type, name='products_of_type'),
    url(r'^add_product/$', views.add_product, name="add_product")
]

# Payment Type Creation
urlpatterns += [
    url(r'^add_payment_type/$', views.add_payment_type, name="add_payment_type")
]