# from django.test import TestCase
from django.test import SimpleTestCase # cause we are not using a database



class SimpleTests(SimpleTestCase):
  def test_index_page_status_code(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)

  # def test_about_page_status_code(self):
  #   response = self.client.get('/about/')
  #   self.assertEqual(response.status_code, 200)



