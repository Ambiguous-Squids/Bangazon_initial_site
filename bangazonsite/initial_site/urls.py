from django.conf.urls import url

from . import views

app_name = 'initial_site'
urlpatterns = [
	url(r'^products/', views.ProductsView.as_view(), name='products'),
]