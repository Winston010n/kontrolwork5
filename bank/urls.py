from django.urls import path

from .views import book_detail, book_list_create


urlpatterns = [
    path("books/", book_list_create, name="book-list"),
    path("books/<int:pk>/", book_detail, name="book-detail"),
]
