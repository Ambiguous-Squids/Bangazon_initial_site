from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^product_detail/(?P<pk>\d+)/', views.productDetailView.as_view(), name='product_detail')
]

# Products View / Creation
urlpatterns += [
    url(r'^$', views.index, name='index'),
    url(r'^products/', views.get_product_types, name='products'),
    url(r'^products_of_type/(?P<pk>\d+)/', views.get_products_of_type, name='products_of_type'),
    url(r'^add_product/$', views.add_product, name="add_product")
]

# Payment Type Creation
urlpatterns += [
    url(r'^add_payment_type/$', views.add_payment_type, name="add_payment_type")
]


urlpatterns += [
    url(r'^register/$', views.register, name='register'),
    url(r'^list_payment_type/$', views.get_payment_type, name="get_payment_type")
]

urlpatterns += [
    url(r'^order/', views.order_detail, name='order'),
    url(r'^add_product_to_order/(?P<pk>\d+)/', views.add_product_to_order, name='add_product_to_order'),
    url(r'^success/', views.success.as_view(), name='success')

]

urlpatterns += [
    url(r'^no_items/', views.no_items, name='no_items'),
]