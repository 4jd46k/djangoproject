from django.test import TestCase
from django.urls import reverse
from .models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            price=10.99,
            stock=100,
            image="example.jpg"
        )
    
    def test_model_fields(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, 10.99)
        self.assertEqual(self.product.stock, 100)
        self.assertEqual(self.product.image, "example.jpg")
    
    def test_model_list_view(self):
        url = reverse("index")  # Update the URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")
        self.assertContains(response, self.product.image)  # Check if image URL is present
        
    def test_model_detail_view(self):
        url = reverse("index")  # Update the URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")
        self.assertContains(response, self.product.image)  # Check if image URL is present
