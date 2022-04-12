from django.test import TestCase
from django.urls import reverse


class TestHome(TestCase):

    def test_home_page(self):
        response = self.client.get(reverse("index"))

        self.assertEqual(response.request["PATH_INFO"], '/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>Welcome to Holiday Homes</h1>')
        self.assertTemplateUsed(response, "index.html")
