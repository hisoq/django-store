from django.forms import ModelForm, ModelMultipleChoiceField
from .models import Shop, Product


class ProductForm(ModelForm):
    shops = ModelMultipleChoiceField(queryset=Shop.objects.all())

    class Meta:
        model = Product
        fields = '__all__'

class ProductUpdateForm(ModelForm):

    class Meta:
        model = Product
        fields = ('price', )