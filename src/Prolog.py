import re

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

	def parse(self, expresion):
		# Ver si es un atomo
		if re.match(r"^[a-z][a-zA-Z0-9]*$", expresion):
			return Atomo(expresion)

		# Ver si es una variable
		elif re.match(r"^[A-Z][a-zA-Z0-9]*$", expresion):
			return Variable(expresion)

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
			
			return Estructura(nombre, args)
		
		# Ver si es una lista de expresiones
		elif re.match(r"^(.+)\s(.+)$", expresion):
			# Obtener la expresion izquierda
			izquierda = re.match(r"^(.+)\s(.+)$", expresion).group(1)
			
			# Obtener la expresion derecha
			derecha = re.match(r"^(.+)\s(.+)$", expresion).group(2)

			# Parsear cada expresion
			izquierda = self.parse(izquierda.strip())
			derecha = self.parse(derecha.strip())

			return [izquierda, derecha]
		
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
		

# expresion = "true"
# expresion = "padre(juan,jose,maria)"
# expresion = 'padre(X,concat(mar,ia))'
expresion = 'abuelo(X,Y) padre(X,Z) padre(Z,Y)'


prolog = Prolog()
expr = prolog.definir(expresion)
print(expr)
for arg in expr.args:
	match arg:
		case Atomo():
			print("Atomo:", arg.nombre)
		case Variable():
			print("Variable:", arg.nombre)
		case Estructura():
			print("Estructura:", arg.nombre)
