from django.conf.urls import url

from . import views

app_name = 'initial_site'
urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^success/', views.LoginSuccess.as_view(), name='success'),
    url(r'^register/', views.Register.as_view(), name='register'),
    url(r'^login/', views.login_user, name='login'),
    url(r'^register_user/', views.register_user, name='register_user'),
    url(r'^logout/', views.logout_user, name= 'logout'),
    url(r'^products/(?P<pk>\d+)/', views.productDetailView.as_view(), name='product_detail'),
    url(r'^products/', views.get_products, name='products'),
    url(r'^add_product/$', views.add_product, name="add_product"),
    url(r'^add_payment_type/$', views.add_payment_type, name="add_payment_type")
]
