from django.forms import ModelForm
from .models import *

class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = ('name', 'addres', 'brand')
