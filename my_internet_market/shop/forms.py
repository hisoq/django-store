from django.contrib.auth.forms import PasswordChangeForm
from django.forms import ModelForm, ModelMultipleChoiceField, modelform_factory, DecimalField
from .models import Shop, Product
from django import forms
from django.forms.widgets import Select
import re

class ProductForm(ModelForm):
    shops = ModelMultipleChoiceField(queryset=Shop.objects.all())

    class Meta:
        model = Product
        fields = '__all__'
        labels = {'title': 'Название товара', 'content': 'Описание товара', 'price': 'Цена'}
        help_texts = {'category': '<<<< Выберите категорию продукта!', 'price': '<<< Цена должна быть больше 0'}
        field_classes = {'price': DecimalField}
        widgets = {'category': Select(attrs={'size': 7})}  # элемент управления на веб странице.


def validate_positive(value):
    if value <= 0:
        raise forms.ValidationError("Цена должна быть больше 0")


class ProductUpdateForm(ModelForm):
    title = forms.CharField(label='Название товара')
    price = forms.DecimalField(label='Цена', max_value=1000000, help_text='Цена должна быть > 0',
                               validators=[validate_positive])
    multiple = forms.DecimalField(label='Количество товара', )
    class Meta:
        model = Product
        fields = ('price', 'title', 'content', 'multiple', )

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and re.search(r'\d', title):
            raise forms.ValidationError("Название продукта не должно содержать цифры.")
        return title
class ProductDeleteForm(ModelForm):
    class Meta:
        model = Product
        fields = ('title', )

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Старый пароль."
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(),
        label="Новый пароль.",
        help_text="Ваш пароль не должен содержать спец. символы (!@#$%^&*()_+{}|:<>?~)."
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label="Повторите новый пароль."
    )

    def clean_new_password(self):
        password = self.cleaned_data.get('new_password1')
        if re.search(r"[!@#$%^&*()_+{}|:<>?~]", password):
            raise forms.ValidationError("Ваш пароль не должен содержать спец. символы (!@#$%^&*()_+{}|:<>?~).")

        return password

    def __init__(self, user, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(user, *args, **kwargs)