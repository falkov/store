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

    def __str__(self):
        return self.title
