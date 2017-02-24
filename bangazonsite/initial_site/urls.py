from django.conf.urls import url
from . import views


# Products View / Creation
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^products/', views.get_products, name='products'),
    url(r'^products/(?P<pk>\d+)/', views.productDetailView.as_view(), name='product_detail'),
    url(r'^add_product/$', views.add_product, name="add_product")
]

# Payment Type Creation
urlpatterns += [
    url(r'^add_payment_type/$', views.add_payment_type, name="add_payment_type")
]