from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls.base import reverse_lazy


from .models import Cliente


class ListPizzariaView(ListView):
    model = Cliente
    template_name = 'pizzaria_view.html'
    fields = '__all__'
    context_object_name = 'clientes'
    success_url = reverse_lazy('pizzaria_view')

class CreateClienteView(CreateView):
    model = Cliente
    template_name = 'index.html'
    fields = '__all__'
    success_url = reverse_lazy('index')

class UpdateClienteView(UpdateView):
    model = Cliente
    template_name = 'index.html'
    fields = '__all__'
    success_url = reverse_lazy('pizzaria_view')

class DeleteClienteView(DeleteView):
    model = Cliente
    template_name = 'pizzaria_del.html'
    success_url = reverse_lazy('pizzaria_view')

