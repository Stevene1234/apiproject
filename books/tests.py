from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title='Book title',
            subtitle='Book subtitle',
            author='The author',
            isbn='1234567891234'
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, 'Book title')
        self.assertEqual(self.book.subtitle, 'Book subtitle')
        self.assertEqual(self.book.author, 'The author')
        self.assertEqual(self.book.isbn, '1234567891234')

    def test_book_listview(self):
        response= self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Book subtitle')
        self.assertTemplateUsed(response, 'books/book_list.html')