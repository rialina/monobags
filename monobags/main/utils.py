from django.views.generic import ListView
from main.models import Product

class HomeMixin(ListView):
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtered_services = self.get_queryset()
        context['services'] = filtered_services
        return context
    
    def get_queryset(self):
        return self.model.objects.all()
    
class CartMixin(ListView):
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtered_services = self.get_queryset()
        context['total_amount'] = f'{sum([service.price for service in filtered_services])} $' if filtered_services else '0.00$'
        context['services'] = filtered_services
        return context
    
    def get_queryset(self):
        return self.model.objects.filter(users=self.request.user)