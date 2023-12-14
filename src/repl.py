from src.Prolog import Prolog

def main():
	print("-------------------------------------------------------------------------------------")
	print("Bienvenido al interprete del subconjunto de Prolog")
	print("Comandos disponibles:")
	print("DEF <expresion> [<expresion>]")
	print("ASK <expresion>")
	print("SALIR")
	print("-------------------------------------------------------------------------------------\n")

	prolog = Prolog()

	while True:
		entrada = input(">>> ").strip().split(" ")
		comando = entrada[0].upper()
		argumentos = " ".join(entrada[1:]) 
		entrada = [comando, argumentos] if argumentos else [comando]

		print(entrada)

		match entrada:
			case ["SALIR"]:
				break

			case ["SALIR", _]:
				break

			case [""]:
				continue
				
			case ["DEF", args]:
				# tokenizar expresion
				print(f"Definiendo expresion...{args}")
				print(prolog.parse(args))

			case ["ASK", args]:
				print(f"Consultando expresion...{args}")

			
			case _:
				print("Comando no reconocido")

if __name__ == "__main__":
	main()