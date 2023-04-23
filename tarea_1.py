def promediar_notas (): 
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))

    promedio = (nota1 + nota2 + nota3) / 3
    if promedio >= 0 and promedio <= 2:
        return 'D'
    elif promedio > 2 and promedio <= 5:
        return 'C'
    elif promedio > 5 and promedio <= 6:
        return 'B'
    elif promedio > 6 and promedio <= 7:
        return 'A'
    else:
        return 'Error en calificaciones'
    
promedio_final = promediar_notas()
print ("Tu promedio final es:", promedio_final)