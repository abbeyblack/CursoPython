def obtener_trimestre(mes):
    if mes < 1 or mes > 12:
        return "El número del mes debe estar entre 1 y 12."
    elif mes <= 4:
        return "El mes " + str(mes) + " pertenece al primer trimestre."
    elif mes <= 8:
        return "El mes " + str(mes) + " pertenece al segundo trimestre."
    else:
        return "El mes " + str(mes) + " pertenece al tercer trimestre."

numero_mes = int(input("Ingrese el número del mes (1-12): "))

trimestre = obtener_trimestre(numero_mes)

print(trimestre)