import unittest
from src.Parser import Parser

class TestParser(unittest.TestCase):
	def setUp(self):
		self.parser = Parser()

	def test_expression_structure_with_atom(self):
		result = self.parser.parse('atom')
		self.assertEqual(result, ('ATOM', 'atom'))

	def test_expression_structure_with_variable(self):
		result = self.parser.parse('VARIABLE')
		self.assertEqual(result, ('VARIABLE', 'VARIABLE'))

	def test_expression_structure_with_structure_list(self):
		result = self.parser.parse('structure(arg1, arg2)')
		self.assertEqual(result, ('STRUCTURE_LIST', ['structure(arg1, arg2)']))

	# def test_expression_structure_with_nested_structure_list(self):
	# 	result = self.parser.parse('structure(arg1, structure(arg2, arg3))')
	# 	self.assertEqual(result, ('STRUCTURE_LIST', [('STRUCTURE', 'structure(arg1, structure(arg2, arg3))')]))

	def test_list_of_expressions(self):
		result = self.parser.parse('atom(X, X)  atom(Y, Y) atom(Z, Z)')
		self.assertEqual(result, ('STRUCTURE_LIST', ['atom(X, X)', 'atom(Y, Y)', 'atom(Z, Z)']))

	def test_invalid_expression(self):
		with self.assertRaises(Exception):
			self.parser.parse('invalid!')

if __name__ == '__main__':
	unittest.main()