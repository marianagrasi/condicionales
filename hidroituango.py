#Condiciones multiples

sensorNivelAgua=int(input("Digite el nivel del agua de la represa: "))

if sensorNivelAgua>0 and sensorNivelAgua<=150:
    print("muy poca agua las puertas estan cerradas")

elif sensorNivelAgua>150 and  sensorNivelAgua<=400:
    print("Operando normalmente")

elif sensorNivelAgua>400 and sensorNivelAgua<=420:
    print("Mucho cuidado revise el nivel del agua")
elif sensorNivelAgua>420:
    print("Correee")
else:
    print("Revise el sensor medida no valida")



