from .models import Customer, Order, OrderItems, PaymentType, Product, ProductType
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User


def cart(request):
	"""
	This class displays the # of items currently in an active order for the active customer/user.
	@asimonia
	"""
	cart_num = 0

	if request.user.is_authenticated():
		try:
			customer_id = Customer.objects.get(user = request.user.id)
			active_order = Order.objects.get(customer = customer_id, active = 1)
			cart_num = OrderItems.objects.filter(order_id=active_order.id).count()
		except:
			cart_num = 0

	return {'cart': cart_num}