class Motocicleta():
    # Atributos de clase
    estado = "nueva"
    motor = False

    # Métodos
    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso, precio):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.precio = precio
        
    def arrancar(self):
        if self.motor:
            print("Se escucha un molesto sonido al girar la llave. El motor ya estaba arrancado.")
        else:
            print("Se ha arrancado el motor. Ruge como un león.")
    
    def detener(self):
        if self.motor:
            print("Se detiene el motor.")
        else:
            print("No puedes parar el motor, porque ya está apagado. ¿No lo oyes?")

motocicleta_karma = Motocicleta(
    matricula="TS-1989",
    combustible_litros=10,
    color="Red",
    marca="Taylor's Version",
    modelo="Vigilante Sh*t",
    numero_ruedas=2,
    peso=10,
    fecha_fabricacion="13/12/1989",
    velocidad_punta= 133,
    precio= 78762
    )

print(f"El numero de ruedas de la motocicleta marca {motocicleta_karma.marca} modelo {motocicleta_karma.modelo} es de {motocicleta_karma.numero_ruedas} y la cantidad de combustible es de {motocicleta_karma.combustible_litros}")


print(f"El precio de la motocicleta marca {motocicleta_karma.marca} modelo {motocicleta_karma.modelo} es de {motocicleta_karma.precio} dolares")




