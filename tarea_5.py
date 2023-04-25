cadena = input("Ingrese una oración con signo de exclamación al final: ")
if cadena.endswith("!"):
    cadena_sin_exclamacion = cadena[:-1]
    print("La oración sin el signo de exclamación es:", cadena_sin_exclamacion)
else:
    print("La oración no termina con un signo de exclamación.")
