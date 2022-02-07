from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import SongViewSet, RatingViewSet


router = routers.DefaultRouter()
router.register('songs', SongViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
