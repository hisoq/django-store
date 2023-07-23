from django.urls import path
from.views import index, products, ProductView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('index/', index, name='index'),
    path('create_product/', ProductView.as_view(), name='create_product'),
    path('update_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('<str:shop_id>/', products, name='products'),
]
#'<int:shop_id>/ - get параметр