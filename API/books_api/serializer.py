from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.pagenumber = validated_data.get('pagenumber', instance.pagenumber)
        instance.publishdate = validated_data.get('publishdate', instance.publishdate)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()
        return instance
