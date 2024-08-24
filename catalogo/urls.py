from django.contrib import admin
from django.urls import  path
from django.views.generic import RedirectView
from django.conf.urls.static import static,settings
from catalogo.views import indexView


urlpatterns = [
    path('', RedirectView.as_view(url='catalogo/',permanent=True)),
    path('catalogo/', indexView, name='index'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
