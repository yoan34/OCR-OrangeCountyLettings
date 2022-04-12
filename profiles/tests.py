from django.test import TestCase
from django.urls import reverse
from .models import Profile
from django.contrib.auth.models import User
from faker import Faker


class TestProfile(TestCase):

    def setUp(self):
        self.fake = Faker()
        self.user = User.objects.create(
            username=self.fake.first_name(),
            password=self.fake.password()
        )
        self.profile = Profile.objects.create(
            favorite_city=self.fake.city(),
            user=self.user
        )

    def test_profile_creation(self):
        profile = Profile.objects.get(id=self.profile.id)
        self.assertEqual(self.profile.user.username, profile.user.username)

    def test_profile_page(self):
        response = self.client.get(reverse("profiles:index"))

        self.assertEqual(response.request["PATH_INFO"], '/profiles/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>Profiles</title>')
        self.assertTemplateUsed(response, "profiles/index.html")
