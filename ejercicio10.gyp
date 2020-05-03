while True:
    lado1 = int(input("Largo del lado 1:"))
    lado2 = int(input("Largo del lado 2:"))
    lado3 = int(input("Largo del lado 3:"))
    if lado1 == lado2 and lado2 == lado3:
        print("El triángulo es equilátero")

    """ iscósceles """
    if lado1 == lado2 and lado3 != lado1:
        print("El triángulo es iscósceles")
    if lado1 == lado3 and lado2 != lado1:
        print("El triángulo es iscósceles")
    if lado2 == lado3 and lado2 != lado1:
        print("El triángulo es iscósceles")

    """ escaleno """
    if lado1 != lado2 and lado1 != lado3 and lado3 != lado2:
        print("El triángulo es escaleno")
