from . models import Ebook
from rest_framework import serializers

class EbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ebook
        fields = ['title', 'author', 'genre', 'review', 'favorite']

class DeletePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ebook
        fields = "__all__"