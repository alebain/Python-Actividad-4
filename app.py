class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

class Camioneta(Vehiculo):
    def __init__(self, color, ruedas, carga):
        super().__init__(color, ruedas)
        self.carga = carga

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, urbana, deportiva):
        super().__init__(color, ruedas)
        self.urbana = urbana
        self.deportiva = deportiva

class Motocicleta(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


coche1 = Coche("Rojo", 4, 200, 2000)
camioneta1 = Camioneta("Azul", 4, 1000)
bicicleta1 = Bicicleta("Verde", 2, True, False)
motocicleta1 = Motocicleta("Negra", 2, 250, 500)

vehiculos = [coche1, camioneta1, bicicleta1, motocicleta1]


def catalogar(vehiculos, ruedas=None):
    if ruedas is None:
        for vehiculo in vehiculos:
            print(f"Clase: {type(vehiculo).__name__}")
            print(f"Color: {vehiculo.color}")
            print(f"Ruedas: {vehiculo.ruedas}")

            if isinstance(vehiculo, Coche):
                print(f"Velocidad: {vehiculo.velocidad} km/h")
                print(f"Cilindrada: {vehiculo.cilindrada} CC")
            elif isinstance(vehiculo, Camioneta):
                print(f"Carga: {vehiculo.carga} kg")
            elif isinstance(vehiculo, Bicicleta):
                print(f"Urbana: {vehiculo.urbana}")
                print(f"Deportiva: {vehiculo.deportiva}")
            elif isinstance(vehiculo, Motocicleta):
                print(f"Velocidad: {vehiculo.velocidad} km/h")
                print(f"Cilindrada: {vehiculo.cilindrada} CC")

            print("---------------------")
    else:
        filtered_vehiculos = [vehiculo for vehiculo in vehiculos if vehiculo.ruedas == ruedas]
        print(f"Se han encontrado {len(filtered_vehiculos)} vehículos con {ruedas} ruedas:")
        for vehiculo in filtered_vehiculos:
            print(f"Clase: {type(vehiculo).__name__}")
            print(f"Color: {vehiculo.color}")
            print(f"Ruedas: {vehiculo.ruedas}")

            if isinstance(vehiculo, Coche):
                print(f"Velocidad: {vehiculo.velocidad} km/h")
                print(f"Cilindrada: {vehiculo.cilindrada} CC")
            elif isinstance(vehiculo, Camioneta):
                print(f"Carga: {vehiculo.carga} kg")
            elif isinstance(vehiculo, Bicicleta):
                print(f"Urbana: {vehiculo.urbana}")
                print(f"Deportiva: {vehiculo.deportiva}")
            elif isinstance(vehiculo, Motocicleta):
                print(f"Velocidad: {vehiculo.velocidad} km/h")
                print(f"Cilindrada: {vehiculo.cilindrada} CC")

            print("---------------------")


catalogar(vehiculos)
print("---------------------")
catalogar(vehiculos, 0)
print("---------------------")
catalogar(vehiculos, 2)
print("---------------------")
catalogar(vehiculos, 4)

try:
    resultado = 10/0
except ZeroDivisionError:
    print("Error: División por cero. No es posible dividir un número por cero.")


def agregar_una_vez(lista, el):
    if el in lista:
        raise ValueError(f"Error: Imposible añadir elementos duplicados => {el}")
    else:
        lista.append(el)

elementos = [1, 5, -2]
try:
    agregar_una_vez(elementos, 10)
    agregar_una_vez(elementos, -2)
    agregar_una_vez(elementos, "Hola")
except ValueError as e:
    print(e)

print(elementos)
