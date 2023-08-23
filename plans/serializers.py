from rest_framework import serializers
from .models import Plan,CustomPlan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"

class CustomPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomPlan
        fields = "__all__"

    def calculate_price(self, no_of_products, storage):
        x = (no_of_products * 0.11) + (storage * 0.2) + 5
        price = x * 31 * 12
        return price