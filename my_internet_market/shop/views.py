from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View, FormView
from .models import Shop, Product
from .forms import ProductForm, ProductUpdateForm, ProductDeleteForm, CustomPasswordChangeForm
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.core.exceptions import NON_FIELD_ERRORS
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required

@login_required()
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

    def form_valid(self, form):

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
    # fields = ['title', 'price', 'content', 'multiple']
    form_class = ProductUpdateForm
    template_name = 'shop/update_product.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        return super().form_valid(form)


def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductDeleteForm(request.POST, instance=product)  # связывает форму с моделью
        if 'no' in request.POST:
            return redirect('index')
        elif 'yes' in request.POST and form.is_valid():
            product.delete()
            return redirect('index')

    form = ProductForm(instance=product)
    return render(request, 'shop/delete_product.html', {'form': form, 'product': product})

class PasswordChangeView(LoginRequiredMixin, PasswordChangeView): # проверка на то что пользователь авторизован
    template_name = 'shop/change_password.html'
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('change_password_done')

    def get_form_kwargs(self):
        kwargs = super(PasswordChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
def change_password_done(request):
    return render(request, 'shop/change_password_done.html')














