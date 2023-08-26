from rest_framework import serializers
from .models import Plan,CustomPlan
import logging


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"

class CustomPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomPlan
        fields = "__all__"

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request_method = self.context['request'].method 
        if request_method == 'GET':
            self.fields['price'].required = False

    def validate(self, value):
        if value['storage'] < 0 or value['no_of_products'] < 0:
            raise serializers.ValidationError('Negative numbers are not allowed')
        return value

    def calculate_price(self, no_of_products, storage):
        x = (no_of_products * 0.11) + (storage * 0.2) + 5
        price = x * 31 * 12
        return price
