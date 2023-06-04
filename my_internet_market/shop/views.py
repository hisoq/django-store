from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from .models import Shop, Product
from .forms import ProductForm



def index(request):
    shops = Shop.objects.select_related('brand').all()
    context = {'shops': shops}
    return render(request, 'shop/index.html', context)


def products(request, shop_id):
    products = Product.objects.filter(shops=shop_id)
    context = {'products': products, 'shop_id': shop_id}
    return render(request, 'shop/products.html', context)


class ProductView(CreateView):
    template_name = 'shop/create_product.html'
    form_class = ProductForm
    success_url = '/shop/index'

    def form_valid(self, form):
        self.object = form.save()
        shops = Shop.objects.filter(shop_id__in=form.data.getlist('shops'))
        self.object.shops.add(*shops)
        return HttpResponseRedirect(self.get_success_url())






# сделать запрос по uuid магазин для получения всех продуктов +
# сделать в by_brand.html кнопку по которой мы будем переходить на url по созданию продукта для магазина
# и сделать это через createview



