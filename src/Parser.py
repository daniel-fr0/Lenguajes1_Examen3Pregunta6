import ply.lex as lex
import ply.yacc as yacc

# Define the list of token names
tokens = ('ATOM', 'VARIABLE', 'STRUCTURE')

# Regular expression rules for simple tokens
t_ATOM      = r'[a-z][a-zA-Z0-9_]*'
t_VARIABLE  = r'[A-Z][a-zA-Z0-9_]*'
t_STRUCTURE = r'[a-z][a-zA-Z0-9_]*\([a-zA-Z0-9_, ]*\)'
t_ignore	= ' \t'

# Error handling rule
def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Parsing rules
def p_expression_structure(p):
	'''expression : structure_list
				  | ATOM
				  | VARIABLE'''
	p[0] = p[1]

def p_structure_list(p):
	'''structure_list : STRUCTURE
					  | structure_list STRUCTURE'''
	if len(p) == 2:  # single structure
		p[0] = [p[1]]
	else:  # structure list
		p[0] = p[1] + [p[2]]

# Error rule for syntax errors
def p_error(p):
	print(f"Syntax error in token '{p.value}'")

# Build the parser
parser = yacc.yacc()