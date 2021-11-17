from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дүкен'
        verbose_name_plural = 'Дүкендер'


class Category(models.Model):
    name = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категориялар'


class Product(models.Model):
    name = models.CharField(max_length=255, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default='NoCategory')
    update_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тауар'
        verbose_name_plural = 'Тауарлар'


class Store(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Қойма'
        verbose_name_plural = 'Қоймалар'