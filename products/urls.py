from django.urls import path
from products.views import  ProductListView, ProductDetailView,ProductFeatureDetailView,ProductFeatureListView,ProductSlugDetailView
from . import views

app_name ='products'

urlpatterns = [
        
    path('product/',ProductListView.as_view(),name = 'product_list'),
    # path('product/<int:pk>/',ProductDetailView.as_view(),name = 'product_detail'),
    path('product/<str:slug>/',ProductSlugDetailView.as_view(),name = 'product_detail'),
    path('featured/',ProductFeatureListView.as_view()),
    path('featured/<int:pk>/',ProductFeatureDetailView.as_view()),
]
