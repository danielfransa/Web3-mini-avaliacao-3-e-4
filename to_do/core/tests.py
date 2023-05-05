from django.test import TestCase
from django.urls import reverse
from django.template.loader import render_to_string

class InitialTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
    
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

class CadastroTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/cadastro')
    
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)