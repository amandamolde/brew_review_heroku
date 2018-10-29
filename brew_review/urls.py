from django.urls import path
from . import views

urlpatterns = [
    path('api/breweries/', views.BreweryList.as_view(), name='brewery-list'),
    path('api/breweries/<int:pk>', views.BreweryDetail.as_view(), name='brewery-detail'),
    path('api/reviews/', views.ReviewList.as_view(), name='review-list'),
    path('api/reviews/<int:pk>', views.ReviewDetail.as_view(), name='review-detail')
]