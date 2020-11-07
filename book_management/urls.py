from django.urls import path
from .views import ListBook, DetailBook


urlpatterns = [
    path('<int:pk>/', DetailBook.as_view()),
    path('', ListBook.as_view()),
]