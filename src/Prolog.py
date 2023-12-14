import re
from src.Parser import Parser

class Atomo():
	def __init__(self, nombre):
		self.nombre = nombre

	def __str__(self):
		return self.nombre
	
	def __repr__(self):
		return self.__str__()

class Variable():
	def __init__(self, nombre):
		self.nombre = nombre

	def __str__(self):
		return self.nombre
	
	def __repr__(self):
		return self.__str__()

class Estructura():
	def __init__(self, nombre, args):
		self.nombre = nombre
		self.args = args
	
	def __str__(self):
		return f"{self.nombre}({', '.join([str(arg) for arg in self.args])})"
	
	def __repr__(self):
		return self.__str__()

class Prolog():
	def __init__(self):
		self.atomos = set()
		self.variables = set()
		self.estructuras = {}
		self.hechos = {}
		self.reglas = {}
		self.parser = Parser()

	def parse(self, expresion):
		try:
			resultado = self.parser.parse(expresion)
		except:
			raise Exception("Error de sintaxis")
		
		# Ver si es un atomo
		if resultado[0] == "ATOM":
			return Atomo(expresion)

		# Ver si es una variable
		elif resultado[0] == "VARIABLE":
			return Variable(expresion)

		# Ver si es una estructura
		elif resultado[0] == "STRUCTURE_LIST" and len(resultado[1]) == 1:
			# Obtener el nombre de la estructura
			nombre = re.match(r"^[a-z][a-zA-Z0-9]*", expresion).group(0)

			# Obtener los argumentos
			argumentos = re.match(r"^[a-z][a-zA-Z0-9]*\((.*)\)$", expresion).group(1)
			
			# Los argumentos son una lista de expresiones separadas por comas
			argumentos = re.split(r",(?![^()]*\))", argumentos)

			# Parsear cada argumento
			args = [self.parse(argumento.strip()) for argumento in argumentos]
			
			return Estructura(nombre, args)
		
		# Ver si es una lista de expresiones
		elif resultado[0] == "STRUCTURE_LIST" and len(resultado[1]) > 1:
			return [self.parse(expresion) for expresion in resultado[1]]
		
		else:
			raise Exception("Expresion de formato inválido")
		
	def definir(self, expresion):
		resultado = self.parse(expresion)

		match resultado:
			case Atomo():
				if resultado.nombre in self.atomos:
					raise Exception("El atomo ya ha sido definido")
				else:
					self.atomos.add(resultado.nombre)

			case Variable():
				if resultado.nombre in self.variables:
					raise Exception("La variable ya ha sido definida")
				else:
					self.variables.add(resultado.nombre)

			case Estructura():
				if resultado.nombre in self.estructuras:
					raise Exception("La estructura ya ha sido definida")
				else:
					self.estructuras[resultado.nombre] = resultado.args

		return resultado