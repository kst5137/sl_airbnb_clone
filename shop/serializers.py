# from rest_framework import serializers
# from .models import Product, ProductImage
#
#
# class ProductImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductImage
#         fields = ['image']
#
#
# class ProductSerializer(serializers.ModelSerializer):
#     images = ProductImageSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Product
#         fields = ['id', 'text', 'location', 'images']
#
#     def create(self, validated_data):
#         images_data = self.context['request'].FILES
#         product = Product.objects.create(**validated_data)
#         for image_data in images_data.getlist('image'):
#             ProductImage.objects.create(product=product, image=image_data)
#         return product