import ply.lex as lex
import ply.yacc as yacc

# Define the list of token names
tokens = ('ATOM', 'VARIABLE', 'STRUCTURE')

# Regular expression rules for simple tokens
t_ATOM      = r'[a-z][a-zA-Z0-9_]*'
t_VARIABLE  = r'[A-Z][a-zA-Z0-9_]*'
t_STRUCTURE = r'[a-z][a-zA-Z0-9_]*\([a-zA-Z0-9_, ]*\)'
t_ignore	= ' \t'

def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)
	raise Exception("Error lexico")

# Lexer para el parser
lexer = lex.lex()

# REGLAS

def p_expression_structure(p):
    '''expression : structure_list
                  | atom
                  | variable'''
    p[0] = p[1]

def p_atom(p):
    'atom : ATOM'
    p[0] = ('ATOM', p[1])

def p_variable(p):
    'variable : VARIABLE'
    p[0] = ('VARIABLE', p[1])

def p_structure_list(p):
	'''structure_list : STRUCTURE
					  | structure_list STRUCTURE'''
	if len(p) == 2:  # single structure
		p[0] = [p[1]]
	else:  # structure list
		p[0] = p[1] + [p[2]]

def p_structure(p):
    'structure : STRUCTURE'
    p[0] = ('STRUCTURE', p[1])

def p_error(p):
	print(f"Syntax error in token '{p.value}'")
	raise Exception("Error sintactico")

# El parser que se va a usar
parser = yacc.yacc()

print(parser.parse("hola"))
print(parser.parse("hola()"))
print(parser.parse("hola(a)"))
print(parser.parse("hola(a, b) adios(c, d)"))
resultado = parser.parse("hola(a, b) adios(c, d)")
print(resultado[0])