#Diccionarios

empty_dict = {}
full_dict = {
    "id": 1,
    "nombre": "Javiera"
}



lista_teo = ['a1', 'b2']
dict_converted = dict(lista_teo)
print(lista_teo, dict_converted)

tuplca_1 = ('a1', 'b2')
print(tuplca_1, dict(tuplca_1))

list_dimensional = [['a',1], ['b', 3]]
print(list_dimensional, dict(list_dimensional))

#obtener elemento

movies = {
  "film": "Pride and Prejudice",
  "director": "Joe Wright",
  "year": 2005
}
x = movies["film"]
print(x)

#añadir elemento

movies["type"] = "adaptation"
print(movies)

#modificar elemento

movies["type"] = "original"
print(movies)

#eliminar elemento

movies.pop("type")
print(movies)

tv_show_empty = dict()
print(tv_show_empty)

tv_show = {
  "name": "Grey's Anatomy",
  "producer": "Shondaland",
  "seasons": 19,
  "protagonist": "Ellen Pompeo",
}
print(tv_show)
for tv in tv_show.values():
    print(tv)

print(tv_show)
for clave, valor in tv_show.items():
    print(clave, valor)

#condicionales

edad = 20
if edad > 10:
    print("Hola Teo")

teo_edad = 3
if teo_edad >=10:
    print("Teo es un perro viejito")
else:
    print("Teo es un perrito joven")