from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

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

    def retrieve(self, request, *args, **kwargs):
        shop = Shop.objects.filter(id=self.kwargs['shop_id'])
        if not shop:
            raise ValidationError(detail='Shop is not found', code=400)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
