from django.urls import path
from.views import index, products, ProductView, ProductUpdateView, delete, PasswordChangeView, change_password_done
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('index/', index, name='index'),
    path('login/', LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/shop/login'), name='logout'),
    path('change_password/', PasswordChangeView.as_view(), name='change_password'),
    path('change_password/done/', change_password_done, name='change_password_done'),
    path('create_product/', ProductView.as_view(), name='create_product'),
    path('update_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:pk>/', delete, name='delete_product'),
    path('<str:shop_id>/', products, name='products'),
]
#'<int:shop_id>/ - get параметр