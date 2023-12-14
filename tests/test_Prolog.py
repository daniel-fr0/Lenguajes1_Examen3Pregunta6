import unittest
from src.Prolog import Prolog, Atomo, Variable, Estructura

class TestProlog(unittest.TestCase):
	def setUp(self):
		self.prolog = Prolog()

	def test_parse_atom(self):
		result = self.prolog.parse('true')
		self.assertIsInstance(result, Atomo)
		self.assertEqual(result.nombre, 'true')

	def test_parse_variable(self):
		result = self.prolog.parse('X')
		self.assertIsInstance(result, Variable)
		self.assertEqual(result.nombre, 'X')

	def test_parse_structure(self):
		result = self.prolog.parse('padre(juan, jose)')
		self.assertIsInstance(result, Estructura)
		self.assertEqual(result.nombre, 'padre')
		self.assertEqual(len(result.args), 2)
		self.assertIsInstance(result.args[0], Atomo)
		self.assertEqual(result.args[0].nombre, 'juan')
		self.assertIsInstance(result.args[1], Atomo)
		self.assertEqual(result.args[1].nombre, 'jose')

	def test_parse_structure_with_variable(self):
		result = self.prolog.parse('padre(X, Y)')
		self.assertIsInstance(result, Estructura)
		self.assertEqual(result.nombre, 'padre')
		self.assertEqual(len(result.args), 2)
		self.assertIsInstance(result.args[0], Variable)
		self.assertEqual(result.args[0].nombre, 'X')
		self.assertIsInstance(result.args[1], Variable)
		self.assertEqual(result.args[1].nombre, 'Y')

	def test_parse_invalid_expression(self):
		with self.assertRaises(Exception):
			self.prolog.parse('invalid!')

	def test_parse_rule(self):
		result = self.prolog.parse('padre(X, Y) padre(Y, X)')
		self.assertEqual(str(result), '[padre(X, Y), padre(Y, X)]')

if __name__ == '__main__':
	unittest.main()