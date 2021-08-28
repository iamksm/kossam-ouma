import os

from django.test import TestCase
from django.urls import reverse

from kossam_ouma.config import settings

DJANGO_SETTINGS_MODULE = os.getenv("DJANGO_SETTINGS_MODULE")


class LandingTest(TestCase):
    def test_views(self):
        import pdb

        pdb.set_trace()
        url = reverse("index")
        response = self.client.get(url)
        assert response.status_code == 200
