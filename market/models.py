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
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категориялар'


class Product(models.Model):
    name = models.CharField(max_length=255, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True, blank=True)
    update_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тауар'
        verbose_name_plural = 'Тауарлар'
