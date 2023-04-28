from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from .models import Category_Galerie, Image_Galerie

class CategoryGalerieTestCase(TestCase):
    def setUp(self):
        self.category = Category_Galerie.objects.create(
            name="Nature",
        )
        self.subcategory = Category_Galerie.objects.create(
            name="Forêt",
            parent_category=self.category
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Nature")
        self.assertEqual(self.subcategory.parent_category, self.category)

    def test_category_str(self):
        self.assertEqual(str(self.category), "Nature")
        self.assertEqual(str(self.subcategory), "Forêt")


class ImageGalerieTestCase(TestCase):
    def setUp(self):
        self.category = Category_Galerie.objects.create(
            name="Nature",
        )

        image_file = SimpleUploadedFile(
            name="test_image.png",
            content=open("images/test_file/test_image.png", "rb").read(),
            content_type="image/png"
        )

        self.image = Image_Galerie.objects.create(
            category=self.category,
            image=image_file
        )

    def test_image_creation(self):
        self.assertEqual(self.image.category, self.category)
        self.assertEqual(self.image.name, "test_image.png")

    def test_image_str(self):
        self.assertEqual(str(self.image), "test_image.png")
