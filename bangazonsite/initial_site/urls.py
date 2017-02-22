from django.conf.urls import url

from . import views

app_name = 'initial_site'
urlpatterns = [
    url(r'^products/', views.get_products, name='products')
]