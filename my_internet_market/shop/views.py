from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.forms import ModelForm
from .forms import ShopForm
from .models import Shop, Brand, Product


def index(request):  # сделать фу-ию на шоп с продуктами!
    shops = Shop.objects.select_related('brand').all()
    context = {'shops': shops}
    return render(request, 'shop/index.html', context)

def products(request, shop_id):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/by_brand.html', context)

class ShopCreateView(CreateView):
    template_name = 'shop/index.html'
    form_class = ShopForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = Brand.objects.all()
        return context


# def by_brand(request, brand_id):
#     bbs = Shop.objects.filter(brand=brand_id)
#     brands = Brand.objects.all()
#     current_brand = Brand.objects.get(pk=brand_id)
#     context = {'bbs': bbs, 'brands': brands, 'current_brand': current_brand}
#     return render(request, 'shop/by_brand.html', context)

# def show_post(request):
#     post = get_object_or_404(Shop)



