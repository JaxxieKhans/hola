notas = []

while True:
    print("Portal de Notas")
    print("1. Añadir notas")
    print("2. Calcular notas")
    
    opcion = int(input("Ingrese la opcion 1/2: "))

    if opcion == 1:
        nota = int(input("Ingrese la cantidad de notas: "))
        for i in range(nota):
            cal = int(input(f"Ingrese la nota {i+1}: "))
            notas.append(cal)
            continue
    
    if opcion == 2:
        print("Calculo de Promedios")
        
        prom = sum(notas)/len(notas)

        print(f"El promedio de notas es: {prom}")