from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from market.models import Category, Shop
from market.serializers.category_serializer import CategorySerializer


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        shop_id = self.kwargs['shop_id']
        category_qs = Category.objects.filter(shop=shop_id)
        return category_qs

    def list(self, request, *args, **kwargs):
        shop_id = self.kwargs['shop_id']
        shop = Shop.objects.filter(id=shop_id)
        if not shop:
            raise ValidationError(detail='Shop is not found', code=400)

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
