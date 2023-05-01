# Python3 code to demonstrate
# to extract words from string
# using split()
     
# initializing string
#test_string = "Es una verdad universalmente conocida..."
     
# printing original string
#print ("El texto original es: " + test_string)
     
# using split()
# to extract words from string
#res = test_string.split()
     
# printing result
#print ("\nLas palabras de la string son:")
#for palabra in res:
#    print(palabra)



#    if palabra != ' ':
 #       print(palabra)
 #   else:
  #      break


def saludar(name):
    print(f'Hola {name} !!!')

def saludar2(first_name, last_name):
    print(f'Hola {first_name} {last_name}!!!')

saludar('Javiera')
saludar2('Javiera', 'Iturrieta')

def mult_text(text, multiplier):
    print(text * multiplier)

mult_text("V", 8)
