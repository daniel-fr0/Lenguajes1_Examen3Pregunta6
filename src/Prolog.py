import re

class Prolog():
	def __init__(self):
		self.atomos = set()
		self.variables = set()
		self.estructuras = {}
		self.hechos = {}
		self.reglas = {}

	def parse(self, expresion):
		# Ver si es un atomo
		if re.match(r"^[a-z][a-zA-Z0-9]*$", expresion):
			if expresion in self.atomos:
				raise Exception("Atomo ya definido")
			
			self.atomos.add(expresion)
			return expresion

		# Ver si es una variable
		elif re.match(r"^[A-Z][a-zA-Z0-9]*$", expresion):
			if expresion in self.variables:
				raise Exception("Variable ya definida")

			self.variables.add(expresion)
			return expresion

		# Ver si es una estructura
		elif re.match(r"^[a-z][a-zA-Z0-9]*\((.+)\)$", expresion):
			# Obtener el nombre de la estructura
			nombre = re.match(r"^[a-z][a-zA-Z0-9]*", expresion).group(0)

			# Obtener los argumentos
			argumentos = re.match(r"^[a-z][a-zA-Z0-9]*\((.*)\)$", expresion).group(1)
			
			# Los argumentos son una lista de expresiones separadas por comas
			argumentos = re.split(r",(?![^()]*\))", argumentos)

			# Parsear cada argumento
			args = [self.parse(argumento.strip()) for argumento in argumentos]
			
			self.estructuras[nombre] = args
			return {"nombre": nombre, "args": args}
		
		else:
			raise Exception("Expresion no reconocida")
		

expresion = "padre(juan, hermanos(jose, maria, pedro))"

prolog = Prolog()
nombre = prolog.parse(expresion)
print(nombre)
