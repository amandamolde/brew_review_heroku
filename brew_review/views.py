from rest_framework import generics

from .models import Brewery, Review
from .serializers import BrewerySerializer, ReviewSerializer

# Create your views here.
class BreweryList(generics.ListCreateAPIView):
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer

class BreweryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all().prefetch_related('brewery')
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all().prefetch_related('brewery')
    serializer_class = ReviewSerializer