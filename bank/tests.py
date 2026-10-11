from rest_framework import status
from rest_framework.test import APITestCase

from .models import Book


class BookApiTests(APITestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Test book",
            author="Test author",
            published_year=2024,
        )

    def test_list_books(self):
        response = self.client.get("/books/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book(self):
        response = self.client.post(
            "/books/",
            {
                "title": "New book",
                "author": "New author",
                "published_year": 2020,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_invalid_book_is_rejected(self):
        response = self.client.post(
            "/books/",
            {"title": "", "author": "Author", "published_year": 2020},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_book_update_is_rejected(self):
        response = self.client.put(
            f"/books/{self.book.pk}/",
            {"title": "", "author": "Author", "published_year": 2020},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_update_and_delete_book(self):
        detail_url = f"/books/{self.book.pk}/"

        get_response = self.client.get(detail_url)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

        put_response = self.client.put(
            detail_url,
            {
                "title": "Updated book",
                "author": "Updated author",
                "published_year": 2021,
            },
            format="json",
        )
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.data["title"], "Updated book")

        delete_response = self.client.delete(detail_url)
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())
