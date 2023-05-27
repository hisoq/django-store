from django.urls import path
from .views import index, products

urlpatterns = [
    path('index/', index),
    path('products/', products),
    # path('add/', ShopCreateView.as_view(), name='add'),
    path('<int:shop_id>/', products, name='products'),
]
#'<int:shop_id>/ - get параметр