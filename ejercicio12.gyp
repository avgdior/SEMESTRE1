temperatura = int(input("Ingrese la temperatura:"))
dia = input("Ingrese el dia:")
if temperatura < 10:
    print("Abriguese mucho")
if temperatura >= 10 and temperatura < 20:
    print("Abrigo moderado")
if temperatura >= 20:
    print("Ropa comoda")
if dia.upper() == "DOMINGO":
    print("Quedese en casa")
else:
    print("vaya a a trabajar")