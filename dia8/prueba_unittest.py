import unittest
import dia8.cambia_texto

class TestCambiaTexto(unittest.TestCase):
    def test_prueba(self):
        self.assertEqual(dia8.cambia_texto.todo_mayusculas('hola'), 'HOLA')
        self.assertEqual(dia8.cambia_texto.todo_mayusculas('Hola'), 'HOLA')
        self.assertEqual(dia8.cambia_texto.todo_mayusculas('HOLA'), 'HOLA')

if __name__ == '__main__':
    unittest.main()

