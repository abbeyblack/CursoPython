numero = 1
while numero <= 10:
    print("Tabla del", numero)
    multiplicador = 1
    while multiplicador <= 10:
        resultado = numero * multiplicador
        print(numero, "x", multiplicador, "=", resultado)
        multiplicador += 1
    numero += 1
    print()

    