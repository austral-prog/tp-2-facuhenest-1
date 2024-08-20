#ejercicio 1
first_name = "AdA"
last_name = "LoVeLAce"

print(first_name.lower(), " ", last_name.lower())
print(first_name.title(), " ", last_name.title())
print(first_name.upper(), " ", last_name.upper())
print("\t" + first_name.lower(), " ", last_name.lower())

#ejercicio 2

X="Barbados"
Y="Bangladesh"
print("The result of ", X, " comes first in the dictionary than", Y, "is", X>Y)
print("The result of ", Y, " comes first in the dictionary than", X, "is", Y>X)

#ejercicio 3

gasto=input("Ingresar gasto:\n")

dinero=input("Dinero recibido \n")

print(" ")
print("Vuelto")
print(" ")
print("Pesos:")
gasto2=float(gasto)
dinero2=float(dinero)
vuelto= dinero2-gasto2
print(vuelto)
print("Centavos:")
centavos=int(((dinero2-gasto2)-int(dinero2-gasto2))*100)

print(centavos)