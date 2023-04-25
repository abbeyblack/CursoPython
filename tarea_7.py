def nota_final(examen, proyectos):
    if examen > 90 or proyectos > 10:
        return 100
    elif examen > 75 and proyectos >= 5:
        return 90
    elif examen > 50 and proyectos >= 2:
        return 75
    else:
        return 0

calificacion = nota_final(80, 6)
print("La calificación final del estudiante es:", calificacion)
