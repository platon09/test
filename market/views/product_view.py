from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

from market.models import Product, Category, Shop
from market.serializers.product_serializer import ProductSerializer


class ProductDetailView(RetrieveUpdateAPIView):
    serializer_class = ProductSerializer

    def get_object(self):
        product = Product.objects.get(id=self.kwargs['prod_id'])
        return product


class ProductListView(ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        shop_id = self.kwargs['shop_id']
        cat_id = self.kwargs['cat_id']
        product_qs = Product.objects.filter(category=cat_id, shop=shop_id)
        return product_qs

    def create_list(self, serializer):
        for item in serializer.data:
            Product.objects.create(**item, category_id=self.kwargs['cat_id'], shop_id=self.kwargs['shop_id'])

    def create(self, request, *args, **kwargs):
        data = request.data
        for item in data:
            item['update_counter'] = 0

        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        self.create_list(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        shop_id = kwargs['shop_id']
        cat_id = kwargs['cat_id']
        category = Category.objects.filter(id=cat_id, shop=shop_id)
        if not category:
            raise ValidationError(detail='Category is not found', code=400)

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
