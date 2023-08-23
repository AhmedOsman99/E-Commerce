from rest_framework import serializers
from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Price must be greater than zero')
        return value
    
    def validate_name(self, value):
        return value['name'].lower()
    
    def create(self, validated_data):
        return super().create(**validated_data)
    
    def update(self,instance , validated_data):
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        image_path = representation['image']
        representation['image'] = f'http://teqneia.com{image_path}'
        return representation
    

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'products']