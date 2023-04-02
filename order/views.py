from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from .models import LaundryItem
from .forms import LaundryItemForm

class IndexView(ListView):
    model = LaundryItem
    template_name = 'order.html'
    context_object_name = 'laundry_items'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return LaundryItem.objects.filter(name__icontains=query)
        return LaundryItem.objects.all()

class CreateItemView(LoginRequiredMixin, CreateView):
    model = LaundryItem
    form_class = LaundryItemForm
    template_name = 'create_item.html'
    success_url = reverse_lazy('laundry:order')

class EditItemView(LoginRequiredMixin, UpdateView):
    model = LaundryItem
    form_class = LaundryItemForm
    template_name = 'edit_item.html'
    success_url = reverse_lazy('laundry:order')

# def generate_invoice(request, pk):
#     customer = get_object_or_404(Customer, pk=pk)
#     laundry_items = customer.laundryitem_set.all()
#     total = sum(item.price for item in laundry_items)
#     context = {
#         'customer': customer,
#         'laundry_items': laundry_items,
#         'total': total,
#     }
#     html = render(request, 'invoice.html', context)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'filename="invoice-{customer.pk}.pdf"'
#     weasyprint.HTML(string=html.content.decode()).write_pdf(response)
#     return response