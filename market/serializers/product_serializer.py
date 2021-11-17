from rest_framework import serializers
from market.serializers.category_serializer import CategorySerializer
from market.models import Product


class ProductSerializer(serializers.ModelSerializer):
    #category = CategorySerializer()
    class Meta:
        model = Product
        fields = ['id', 'name', 'update_counter']

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.update_counter += 1
        instance.save()
        return instance
