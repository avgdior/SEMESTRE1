while True:
    numero = int(input("Ingrese un numero"))
    if numero % 7 == 0:
        print("El numero es multiplo de 7")
        if numero % 3 == 0:
            print("El numero es multiplo de 3")
        else:
            print("Es multiplo de 7 pero no de 3")
    else:
        print("No es multiplo de 7")
        if numero % 3 == 0:
            print("Pero es multiplo de 3")