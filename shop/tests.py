from django.test import TestCase
from django.urls import reverse

from .models import Cliente, pedido


class InicioViewTests(TestCase):
    def test_homepage_displays_orders_and_uses_static_stylesheet(self):
        cliente = Cliente.objects.create(
            nombre='Ana',
            email='ana@example.com',
        )
        pedido.objects.create(
            producto='Pastas',
            url='https://example.com/pastas.jpg',
            cliente=cliente,
            fecha='2026-10-12T12:00:00Z',
            cantidad=2,
            total=12000,
        )

        response = self.client.get(reverse('inicio'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inicio.html')
        self.assertContains(response, 'RESTAURANTE EL INSACIABLE')
        self.assertContains(response, 'Pastas')
        self.assertContains(response, 'Ana')
        self.assertContains(response, 'https://example.com/pastas.jpg')
        self.assertContains(response, 'Todos los derechos reservados, 2026')
        self.assertContains(response, '/static/style.css')
