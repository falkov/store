from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """Категории товаров"""
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children')
    slug = models.SlugField(max_length=100, unique=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель товара"""
    categoru = models.ForeignKey(Category, verbose_name='Категория товара', on_delete=models.CASCADE)
    title = models.CharField('Название товара', max_length=150)
    description = models.TextField('Описание товара')
    price = models.IntegerField('Цена товара', default=0)
    slug = models.SlugField(max_length=150)
    availability = models.BooleanField('Наличие товара')
    quantity = models.IntegerField('Количество товара на складе', default=1)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['title']

    def __str__(self):
        return self.title


class Cart(models.Model):
    """ Корзина """
    user = models.ForeignKey(User, verbose_name='Покупатель', on_delete=models.CASCADE)
    accepted = models.BooleanField(verbose_name='Принято к заказу', default=False)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class CartItem(models.Model):
    """ Товары в корзине """
    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    quantity = models.IntegerField('кол.', default=0)

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'


class Order(models.Model):
    """ Заказ """
    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE)
    accepted = models.BooleanField(verbose_name='Заказ выполнен', default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
