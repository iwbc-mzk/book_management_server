from django.urls import path, include
from .views import BookViewSet, AuthorViewSet, SeriesViewSet, PublisherViewSet, LabelViewSet, MediumViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'series', SeriesViewSet)
router.register(r'publisher', PublisherViewSet)
router.register(r'label', LabelViewSet)
router.register(r'medium', MediumViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

