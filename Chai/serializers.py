from rest_framework import serializers
from .models import Chai, Order, OrderItem

class ChaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chai
        fields = ['id', 'name', 'price', 'short_Description', 'type']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['chai_name', 'price', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'created_at', 'total', 'items']