from django.forms import ModelForm, ModelMultipleChoiceField
from .models import Shop, Product

# class ShopForm(ModelForm):
#     class Meta:
#         model = Shop
#         fields = ('name', 'addres', 'brand')

class ProductForm(ModelForm):
    shops = ModelMultipleChoiceField(queryset=Shop.objects.all())
    class Meta:
        model = Product
        fields = '__all__'