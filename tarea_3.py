def mcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        r = a % b
        a, b = b, r

    return a

a = 24
b = 36
resultado = mcd(a, b)
print("El MCD de", a, "y", b, "es", resultado)
