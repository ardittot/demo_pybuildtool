""" Tests for ContentNews
"""

from django.test import TestCase
from django.urls import reverse

class ContentNewsViewsTests(TestCase):
    """ Tests ContentNews views.
    """

    def test_list_view(self):
        """ Test if /news responsive
        """

        response = self.client.get(reverse('news:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'hallo!')
