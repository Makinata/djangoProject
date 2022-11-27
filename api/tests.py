from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase


# Create your tests here.
class Query_broker_Tests(APITestCase):
    def test_query_correct(self): # Проверка вывода с корректным запросом
        url = reverse('query_broker', args=['select * from place'])
        response = self.client.get(url)
        self.assertEqual(response.data, {
            "req": "select * from place",
            "resp": "[('Концертный зал', 200, 'Аудио, свет'), ('Коворкинг', 50, 'Проектор'), ('Спортивный зал', 50, 'Спортинвентарь'), ('Площадь', 500, None)]"
        })

    def test_query_error(self): # Проверка вывода с корректным запросом
        url = reverse('query_broker', args=['123'])
        response = self.client.get(url)
        self.assertEqual(response.data, {
            "req": "123",
            "resp": 'near "123": syntax error'
        })

    def test_empty_error(self): # Проверка вывода с корректным запросом
        url = reverse('query_broker', args=[' '])
        response = self.client.get(url)
        self.assertEqual(response.data, {
            "req": " ",
            "resp": '[]'
        })

    def test_args_error(self): # Проверка вывода с корректным запросом
        url = reverse('query_broker', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.data, {
            "req": '1',
            "resp": 'near "1": syntax error'
        })


