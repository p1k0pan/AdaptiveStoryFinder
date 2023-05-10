from rest_framework import serializers

from .models import Article

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'titel', 'thumbnail', 'views', 'release_date', 'author', 'description', 'text', 'num_sections', 'num_images')