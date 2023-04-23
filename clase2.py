first_name = "Javiera"
last_name = "Iturrieta"
print(first_name + last_name)

print(first_name * 3)

mensaj3 = "Paz"
print (mensaj3)
mensaj3 += ","
print (mensaj3)
mensaj3 += "Clavijo"
print (mensaj3)


txt = "It iS A TrUtH UnIvErSaLlY AcKnOwLeDgEd "

x = txt.lower()

print(x)


s = "Javiera"
new_s = s.replace('a','o')
print(new_s)


print(list("Concurso"))

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)

print ("======= Listas ===")

empty_list = []
print(empty_list)

fullfiled_list = [1, 3, 500, 1.4, [2, "a"], {"name": "Javi"}, (1, 3, 5)] 
print(fullfiled_list)


second_list = list()
print(second_list)

numeros = [1, 4, 6]
numeros.append(10)
print(numeros)

print(numeros[2])

lista = ["aries","tauro","geminis","cancer","leo","virgo","libra","escorpio","sagitario","capricornio","acuario","piscis"]
for y in lista:
  print(y)