from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from market.models import Store, Product, Category, Shop
from market.serializers.product_serializer import ProductSerializer


class ProductDetailView(RetrieveUpdateAPIView):
    serializer_class = ProductSerializer

    def get_object(self):
        queryset = Product.objects.get(id=self.kwargs['prod_id'])
        return queryset


class ProductListView(ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        shop_id = self.kwargs['shop_id']
        cat_id = self.kwargs['cat_id']
        store_set = Store.objects.filter(shop=shop_id, product__category=cat_id)
        queryset = []
        for obj in store_set:
            prod = obj.product
            if queryset.count(prod) == 0:
                queryset.append(prod)
        return queryset

    def create(self, request, *args, **kwargs):
        shop_id = self.kwargs['shop_id']
        cat_id = self.kwargs['cat_id']
        for req in request.data:
            prod = Product.objects.create(
                name=req['name'],
                category=Category.objects.get(id=cat_id))
            prod.save()
            store = Store.objects.create(shop=Shop.objects.get(id=shop_id), product=prod)
            store.save()

        """
        if not Category.objects.filter(name=cat_name).exists():
            cat = Category.objects.create(name=cat_name).save()
            prod = Product.objects.create(name=req['name'], category=cat).save()
            Store.objects.create(shop=Shop.objects.get(id=shop_id), product=prod).save()
        else:
            prod = Product.objects.create(
                name=req['name'],
                category=Category.objects.get(name=cat_name)).save()
            Store.objects.create(shop=Shop.objects.get(id=shop_id), product=prod).save()
        """
        return Response(self.queryset)
