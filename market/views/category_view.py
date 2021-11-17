from rest_framework.generics import ListAPIView, RetrieveAPIView

from market.models import Category, Store
from market.serializers.category_serializer import CategorySerializer


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        shop_id = self.kwargs['shop_id']
        store_set = Store.objects.filter(shop=shop_id)
        queryset = []
        for obj in store_set:
            try:
                cat = obj.product.category
                if queryset.count(cat) == 0:
                    queryset.append(cat)
            except:
                continue
        return queryset
