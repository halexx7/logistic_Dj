from django.core.management import call_command
from django.test import TestCase
from django.test.client import Client

from authnapp.models import ShopUser
from mainapp.models import Services, ServicesCategory


class TestMainappSmoke(TestCase):
    fixtures = [
        "mainapp/fixtures/001_dump_category.json",
        "mainapp/fixtures/002_dump_services.json",
        "mainapp/fixtures/006_dump_contacts.json",
        "authnapp/fixtures/admin_user.json",
    ]

    def setUp(self):
        self.client = Client()

    def test_fixtures_load(self):
        # Check fixtures loading
        self.assertGreater(ServicesCategory.objects.count(), 0)
        self.assertGreater(Services.objects.count(), 0)

    def test_mainapp_urls(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/services/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/services/category/0/")
        self.assertEqual(response.status_code, 200)

        for category in ServicesCategory.objects.all():
            response = self.client.get(f"/services/category/{category.pk}/")
            self.assertEqual(response.status_code, 200)

        for service in Services.objects.all():
            response = self.client.get(f"/services/service/{service.pk}/")
            self.assertEqual(response.status_code, 200)


class ProductsTestCase(TestCase):
    def test_product_print(self):
        product_1 = Services.objects.get(name="Gazel NEXT")
        product_2 = Services.objects.get(name="Volvo FH550")
        self.assertEqual(str(product_1), "Gazel NEXT (Ground)")
        self.assertEqual(str(product_2), "Volvo FH550 (Ground)")

    def test_product_get_items(self):
        product_1 = Services.objects.get(name="Gazel NEXT")
        product_3 = Services.objects.get(name="Volvo FH550")

        products_as_class_method = set(product_1.get_items())
        products = set([product_1, product_3])

        self.assertIsNotNone(products_as_class_method.intersection(products))
