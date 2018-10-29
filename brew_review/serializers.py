from rest_framework import serializers
from .models import Brewery, Review

class BrewerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brewery
        fields = ('id', 'name', 'city', 'state', 'description', 'website_url', 'photo_url')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'brewery', 'atmosphere', 'beer_tenders', 'beer_selection', 'notes', )