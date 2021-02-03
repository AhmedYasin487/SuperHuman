from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView
from django.db.models import Q
# Create your views here.

class SearchProductListView(ListView):
    model = Product
    template_name = "search/view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get('q')
        return context
    
    def get_queryset(self,*args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q',None)

        if query is not None:
            loopups = Q( title__icontains = query)|Q(description__icontains = query)|Q(price__icontains = query)|Q(tag__title__icontains = query)
            return Product.objects.filter(loopups).distinct()
        return Product.objects.featured() 
    
