from django.test import TestCase
from django.urls import reverse

from kossam_ouma.landing.views import index


class TestViews(TestCase):
    def test_index(self):
        url = reverse(index)
        resp = self.client.get(url)
        assert resp.status_code == 200
