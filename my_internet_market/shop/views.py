from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from .models import Shop, Product
from .forms import ProductForm, ProductUpdateForm
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

def index(request):  #  Заменить на ListView
    shops = Shop.objects.select_related('brand').all()
    paginator = Paginator(shops, 2)
    page_num = request.GET.get('page', 1)
    page = paginator.get_page(page_num)
    print(page_num)
    context = {'shops': page.object_list, 'page': page}
    return render(request, 'shop/index.html', context)


def products(request, shop_id):  #  Заменить на DetailView
    products = Product.objects.filter(shops=shop_id)
    context = {'products': products, 'shop_id': shop_id}
    return render(request, 'shop/products.html', context)


class ProductView(CreateView):
    template_name = 'shop/create_product.html'
    form_class = ProductForm
    success_url = '/shop/index'

    def form_valid(self, form):    #сюда гетпараметр

        price = form.cleaned_data.get('price')
        if price <= 0:
            form.add_error('price', 'Цена должна быть больше 0')
            return self.form_invalid(form)

        self.object = form.save()
        shops = Shop.objects.filter(shop_id__in=form.data.getlist('shops'))
        self.object.shops.add(*shops)
        return HttpResponseRedirect(self.get_success_url())

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['title', 'price', 'content', 'multiple']
    template_name = 'shop/update_product.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        return super().form_valid(form)
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'shop/delete_product.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):

        return super().form_valid(form)


















