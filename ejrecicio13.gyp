"""
13.Se ingresan notas de curso de un grupo de estudiantes.
Luego de cada ingreso mostrar la información actualizada indicando cuántos pasan a exámen ( nota < 70 ), cuántos exoneran el exámen ( nota > = 70 ) y cuántos sacaron una muy buena nota ( > 90 ).
A su vez indicar cuál fue el promedio de notas, la nota máxima y la mínima. El programa finaliza cuando se ingresa una nota menor que cero.
"""
uno = 0
aexamen = 0
exoneran = 0
buenanota = 0
suma = 0
lista = []
while uno >= 0:
    lista.append(int(input("Agregue una nota o un numero negativo para finalizar:")))
    print(lista)
    uno = uno + 1
    
    if lista[-1] <= -1:
        lista.remove(-1)
        print(lista)
        print("La cantidad de notas es", len(lista))
        for i in lista:
            if i < 70:
                aexamen = aexamen + 1
            if i >= 70:
                exoneran = exoneran + 1
            if i > 90:
                buenanota = buenanota + 1 
        for i in lista:
            suma = suma + i
        print(aexamen,"alumnos deben rendir examen")
        print(exoneran,"alumnos exoneran")
        print(buenanota,"alumnos sacaron buena nota")
        print("El promedio es:",suma / len(lista))
        print(max(lista),"fue la nota mas alta")
        print(min(lista),"fue la nota mas baja")