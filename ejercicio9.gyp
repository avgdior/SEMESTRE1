print("1 - Para convertir de F a C")
print("2 = Para convertir de C a F")
opcion = int(input(":"))
if opcion == 1:
    fah = int(input("Valor en Fahrenheit a convertir:"))
    print(fah,"en celcius es:",(fah - 32) * (5/7))
elif opcion == 2:
    cels = int(input("Valor en Celsius a convertir:"))
    print(cels,"en fahrenheit es:",(cels * (9/5) + 32))