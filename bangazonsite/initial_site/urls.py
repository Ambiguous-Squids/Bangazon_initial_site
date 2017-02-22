from django.conf.urls import url

from . import views

app_name = 'initial_site'
urlpatterns = [
    url(r'^products/(?P<pk>\d+)/', views.productDetailView.as_view(), name='product_detail'),
    url(r'^products/', views.get_products, name='products')
]