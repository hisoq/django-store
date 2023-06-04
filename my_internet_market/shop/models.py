from django.db import models
import uuid

class Shop(models.Model):
    shop_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    products = models.ManyToManyField('Product', related_name='shops')
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, verbose_name='Франшиза')
    name = models.CharField(max_length=20, unique=True, verbose_name='Название магазина')
    #slug = models.SlugField(max_length=20, unique=True, db_index=True, verbose_name='URL')
    addres = models.CharField(max_length=20, null=False,  verbose_name="Адрес")

    class Meta:
        db_table = 'Shop'
        verbose_name_plural = 'Магазины'
        verbose_name = 'Магазин'

    def __str__(self):
        return f'{self.name} - {self.addres}'

class Product(models.Model):

    CREALCE = 'крупы'
    MILK = 'молоко'
    MEAT = 'мясо'
    FISH = 'рыба'
    FRUITS = 'фрукты'
    VEGE = 'овощи'
    ALKOHOL = 'алкоголь'
    TYPE_PRODUCT = (
        (CREALCE, 'Крупы'),
        (MILK, 'Молочная продукция'),
        (MEAT, 'Мясо'),
        (FISH, 'Рыба'),
        (FRUITS, 'Фрукты'),
        (VEGE, 'Овощи'),
        (ALKOHOL, 'Алкоголь'),
    )

    category = models.CharField(max_length=8, choices=TYPE_PRODUCT, default=MILK, verbose_name='Тип продукта:')
    title = models.CharField(max_length=30, verbose_name='Название товара: ')
    content = models.TextField(null=True, blank=True, verbose_name='Описание товара')
    price = models.IntegerField(null=True, blank=True, verbose_name='Цена за еденицу')
    shipment = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата поставки")

    class Meta:
        db_table = 'Product'
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукт'

    def __str__(self):
        return f'{self.title} - {self.category}'

class Brand(models.Model):
    ZOOSHOP = 'Зоомагазин'
    APTEKA = 'Аптека'
    CLOTHING = 'Магазин одежды'
    HOUSEHOLD = 'Товары для дома'
    PRODUCT = 'Продуктовый'
    TYPE_SHOP = (
        (ZOOSHOP, 'Зоомагазин'),
        (APTEKA, 'Аптека'),
        (CLOTHING, 'Магазин одежды'),
        (HOUSEHOLD, 'Товары для дома'),
        (PRODUCT, 'Продуктовый'),
    )

    name = models.CharField(max_length=20, db_index=True, verbose_name='Франшиза')
    typeshop = models.CharField(max_length=20, choices=TYPE_SHOP, default=PRODUCT, verbose_name='Тип мигазина')

    class Meta:
        db_table = 'Brand'
        verbose_name_plural = 'Франшизы'
        verbose_name = 'Франшиза'

    def __str__(self):
        return f'{self.name}'


