from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import CreateClienteView, ListPizzariaView, UpdateClienteView, DeleteClienteView

from .viewsets import PizzariasView, PizzariaView

urlpatterns = [
    path('', CreateClienteView.as_view(), name='index'),
    path('list/', login_required (ListPizzariaView.as_view()), name='pizzaria_view'),
    path('<int:pk>/pizzaria_update/', login_required (UpdateClienteView.as_view()), name='pizzaria_update'),
    path('<int:pk>/pizzaria_delete/', login_required (DeleteClienteView.as_view()), name='pizzaria_delete'),
    path('apilist/', PizzariasView.as_view(), name="listaapi"),
    path('apilist/<int:pk>', PizzariaView.as_view(), name="detailapi")
]