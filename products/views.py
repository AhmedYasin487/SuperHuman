from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.http import Http404
from .models import Product
from carts.models import Cart
# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"

    def get_context_data(self, **kwargs):
        context = super(ProductListView,self).get_context_data(**kwargs)
        # print(context)
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView,self).get_context_data(**kwargs)
        
        return context
    def get_object(self,*args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product is not here ")
        return instance

    
class ProductFeatureListView(ListView):
    model = Product
    template_name = "products/product_list.html"

    def get_queryset(self,*args, **kwargs):
        request = self.request
        return Product.objects.featured()

class ProductFeatureDetailView(DetailView):
    queryset= Product.objects.featured()
    model = Product
    template_name = "products/featured_detail.html"

    # def get_queryset(self,*args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()

class ProductSlugDetailView(DetailView): 
    queryset= Product.objects.featured()
    template_name = "products/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProductSlugDetailView,self).get_context_data(**kwargs)
        cart_obj,new_obj = Cart.objects.new_or_get(self.request)
        context["cart"] = cart_obj
        return context 
    
    def get_object(self,*args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise Http404("Product is not here ")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404("Nahh hummmm ")
        

        return instance
 