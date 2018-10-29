from django.urls import path
from . import views

urlpatterns = [
    path('breweries/', views.BreweryList.as_view(), name='brewery-list'),
    path('breweries/<int:pk>', views.BreweryDetail.as_view(), name='brewery-detail'),
    path('reviews/', views.ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>', views.ReviewDetail.as_view(), name='review-detail')
]