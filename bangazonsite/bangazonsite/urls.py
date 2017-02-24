from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from django.contrib import admin

from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bangazon/', include('initial_site.urls')),
    url(r'^$', RedirectView.as_view(url='/bangazon/', permanent=True)),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    url('^accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
