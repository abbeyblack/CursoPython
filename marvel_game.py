
is_human = input("¿Es humano?")
can_fly = input("¿Puede volar?")
wears_mask = input("¿Usa mascara?")

if is_human == "si":
    if wears_mask == "si":
        print("Black Widow!")
    else:
        print("Captain America!")
else:
    if can_fly == "si":
        print("Thor!")
    elif wears_mask == "no":
        print("Gamora!")
    else:
        print("Rocket!")

#break
want_exit = "n"
num_questions = 0
while want_exit == "n":
    print("Hello")
    want_exit = input ("¿Quieres salir S/N?")
    num_questions += 1
    if num_questions == 4:
        print("Máximo permitido")
        break
print("while over")
