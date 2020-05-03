listado = []
uno = 1
while uno == 1:
    print("1- Ingresar producto")
    print("2- Listar productos")
    print("3- Salir")
    opcion = int(input("Seleccione una opcion:"))
    if opcion == 1:
        listado.append(input("nuevo producto:"))
    if opcion == 2:
        print(listado)
    if opcion == 3:
        print("Adios")
        uno = -3
    if opcion != 1 and opcion != 2 and opcion != 3:
        print("Opcion no válida")