def calculadora():
    while True:
        valor1 = int(input("Ingrese un valor:"))
        operacion = input("Ingrese una operacion ( “S” para suma, “R” para resta, “M” para multiplicaciòn, “D” para división y “P” para potencia)")
        valor2 = int(input("Ingrese otro valor:"))
        if operacion.upper() == "S":
            print(valor1 + valor2)
        elif operacion.upper() == "R":
            print(valor1 - valor2)
        elif operacion.upper() == "M":
            print(valor1 * valor2)
        elif operacion.upper() == "D":
            print(valor1 / valor2)
        elif operacion.upper() == "P":
            print(valor1 ** valor2)
        else:
            print("Equivocado")
calculadora()