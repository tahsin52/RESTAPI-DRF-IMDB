from django.urls import path, include
# from .views import movie_list, movie_details
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAPI.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetail.as_view(), name='movie-details'),

    path('', include(router.urls)),

    # path('stream/', StreamPlatformAPI.as_view(), name='stream-list'),
    # path('stream/<int:pk>', StreamPlatformDetail.as_view(), name='streamplatform-detail'),

    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')

    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

]