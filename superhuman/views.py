from django.views.generic import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin

class TestView(TemplateView,LoginRequiredMixin):

    
    template_name = "test.html"

class ThanksView(TemplateView):
    template_name = "thank.html"

class HomeView(TemplateView):
    template_name = "index.html"
    
    




