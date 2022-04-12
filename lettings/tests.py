from django.test import TestCase
from django.urls import reverse
from .models import Address, Letting
from faker import Faker


class TestLetting(TestCase):
    def setUp(self):
        self.fake = Faker()
        self.address = Address.objects.create(
            number=self.fake.building_number(),
            street=self.fake.street_name(),
            city=self.fake.city(),
            state=self.fake.name(),
            zip_code=self.fake.postcode(),
        )
        self.letting = Letting.objects.create(
            title=self.fake.name(),
            address=self.address
        )

    def test_letting_creation(self):
        letting = Letting.objects.get(id=self.letting.id)
        self.assertEqual(self.letting.title, letting.title)

    def test_letting_page(self):
        response = self.client.get(reverse("lettings:index"))

        self.assertEqual(response.request["PATH_INFO"], '/lettings/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>Lettings</title>')
        self.assertTemplateUsed(response, "lettings/index.html")
