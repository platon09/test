from rest_framework.generics import ListAPIView, RetrieveAPIView

from market.models import Shop
from market.serializers.shop_serializer import ShopSerializer


class ShopListView(ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ShopDetailView(RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def get_object(self):
        shop = Shop.objects.get(id=self.kwargs['shop_id'])
        return shop
