from django.test import TestCase
from blog.models import CategoryBlog, ArticleBlog
from datetime import datetime

class CategoryBlogModelTests(TestCase):

    def test_category_creation(self):
        category = CategoryBlog.objects.create(name="Test Category")
        self.assertEqual(str(category), category.name)
        self.assertEqual(category.slug, "test-category")

    def test_category_unique_slug(self):
        CategoryBlog.objects.create(name="Test Category")
        duplicate_category = CategoryBlog(name="Test Category")
        with self.assertRaises(Exception):
            duplicate_category.save()


class ArticleBlogModelTests(TestCase):

    def setUp(self):
        self.category = CategoryBlog.objects.create(name="Test Category")

    def test_article_creation(self):
        article = ArticleBlog.objects.create(
            title="Test Article",
            category=self.category,
            intro="This is a test intro.",
            content="This is a test content.",
            publication_time=datetime.now()
        )
        self.assertEqual(str(article), article.title)
        self.assertEqual(article.category, self.category)

    def test_article_without_category(self):
        article = ArticleBlog.objects.create(
            title="Test Article",
            intro="This is a test intro.",
            content="This is a test content.",
            publication_time=datetime.now()
        )
        self.assertEqual(str(article), article.title)
        self.assertIsNone(article.category)

