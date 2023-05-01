import random

# Define constants
VALOR_PASAJE= 730
ADULTO_MAYOR_DISCOUNT = 0.5
PATENTE_BUS = ["TS-1989", "JI-1995", "CV-1994", "AC-1969", "BG-1938"]

# Define counters for each bus
bus_counts = {"TS-1989": {"mujeres": 0, "hombres": 0, "niños": 0, "adulto_mayor": 0, "ingresos": 0},
              "JI-1995": {"mujeres": 0, "hombres": 0, "niños": 0, "adulto_mayor": 0, "ingresos": 0},
              "CV-1994": {"mujeres": 0, "hombres": 0, "niños": 0, "adulto_mayor": 0, "ingresos": 0},
              "AC-1969": {"mujeres": 0, "hombres": 0, "niños": 0, "adulto_mayor": 0, "ingresos": 0},
              "BG-1938": {"mujeres": 0, "hombres": 0, "niños": 0, "adulto_mayor": 0, "ingresos": 0}}

total_counts = {"mujeres": 0, "hombres": 0, "niños": 0, "adulto_mayor": 0}

# Define function to simulate a pasajero boarding the bus
def sube_bus(patente_bus):
    # Generate a random pasajero
    pasajero = random.choice(["woman", "man", "kid", "adulto_mayor"])
    
    # Update the counters based on the pasajero's age and type
    if pasajero == "kid":
        bus_count = bus_counts[patente_bus]
        bus_count["niños"] += 1
        total_counts["niños"] += 1
    elif pasajero == "adulto_mayor":
        bus_count = bus_counts[patente_bus]
        bus_count["adulto_mayor"] += 1
        total_counts["adulto_mayor"] += 1

    elif pasajero == "woman":
        bus_count = bus_counts[patente_bus]
        bus_count["mujeres"] += 1
        total_counts["mujeres"] += 1

    else:
        bus_count = bus_counts[patente_bus]
        bus_count["hombres"] += 1
        total_counts["hombres"] += 1

    
    # Calculate the ticket price based on the pasajero's age and type
    if pasajero == "kid":
        valor_pasaje= 0
    elif pasajero == "adulto_mayor":
        valor_pasaje= VALOR_PASAJE* ADULTO_MAYOR_DISCOUNT
    else:
        valor_pasaje = VALOR_PASAJE
    
    return valor_pasaje

# Simulate 1000 pasajeros boarding each bus
for i in range(1000):
    for patente_bus in PATENTE_BUS:
        bus_counts[patente_bus]["ingresos"] += sube_bus(patente_bus)

# Print the daily report for each bus
for patente_bus in PATENTE_BUS:
    print(f"El reporte del bus patente {patente_bus} es el siguiente")
    print(bus_counts[patente_bus])

# Print the total counts for all the buses
print("El total de personas que tomaron los buses es:")
print(total_counts)
