from django.urls import path
from.views import index, products, ProductView

urlpatterns = [
    path('index/', index),
    path('create_product/', ProductView.as_view(), name='create_product'),
    path('<str:shop_id>/', products, name='products'), #get параметр
]
#'<int:shop_id>/ - get параметр