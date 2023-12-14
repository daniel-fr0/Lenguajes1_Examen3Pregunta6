import ply.lex as lex
import ply.yacc as yacc

class Parser:
	tokens = ('ATOM', 'VARIABLE', 'STRUCTURE', 'LPAREN', 'RPAREN', 'COMMA')

	t_LPAREN = r'\('
	t_RPAREN = r'\)'
	t_COMMA  = r','
	t_ATOM      = r'[a-z][a-zA-Z0-9_]*'
	t_VARIABLE  = r'[A-Z][a-zA-Z0-9_]*'
	t_STRUCTURE = r'[a-z][a-zA-Z0-9_]*\([a-zA-Z0-9_, ]+\)'
	t_ignore    = ' \t'

	def t_error(self, t):
		print("Illegal character '%s'" % t.value[0])
		t.lexer.skip(1)
		raise Exception("Error lexico")

	def __init__(self):
		self.lexer = lex.lex(module=self)
		self.parser = yacc.yacc(module=self)
		self.parse = self.parser.parse

	def p_expression_structure(self, p):
		'''expression : structure_list
					  | atom
					  | variable'''
		p[0] = p[1]

	def p_atom(self, p):
		'atom : ATOM'
		p[0] = ('ATOM', p[1])

	def p_variable(self, p):
		'variable : VARIABLE'
		p[0] = ('VARIABLE', p[1])

	def p_structure(self, p):
		'''structure : atom LPAREN arg_list RPAREN'''
		p[0] = ('STRUCTURE', f'{p[1]}({p[3]})')

	def p_arg_list(self, p):
		'''arg_list : arg
					| arg_list COMMA arg'''
		if len(p) == 2:  # single argument
			p[0] = p[1]
		else:  # argument list
			p[0] = f'{p[1]}, {p[3]}'

	def p_arg(self, p):
		'''arg : ATOM
			   | VARIABLE
			   | STRUCTURE'''
		p[0] = p[1]

	def p_structure_list(self, p):
		'''structure_list : STRUCTURE
						  | structure_list STRUCTURE'''
		if len(p) == 2:  # single structure
			p[0] = ('STRUCTURE_LIST', [p[1]])
		else:  # structure list
			p[0] = ('STRUCTURE_LIST', p[1][1] + [p[2]])

	def p_error(self, p):
		print(f"Syntax error in token '{p.value}'")
		raise Exception("Error sintactico")