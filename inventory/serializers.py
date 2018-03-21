from .models import Product, Comments
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Comments
        fields = ('id', 'title', 'comments', 'rating', 'created_by')


class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'comments')
