nombreCliente=input("Cual es su nombre?")
paisCliente=input("Cual es su pais de origen? ")
cantidadPersonas=int(input("Cuantas personas van a reservar? "))
anoNacimientoCliente=int(input("En que a.o nacio? "))

#Calcular la edad del cliente
anoActual=2024
edadCliente=anoActual-anoNacimientoCliente

#CLASIFICAR, PREGUNTAR, DECIDIR 
if edadCliente >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")
    


