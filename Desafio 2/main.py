from paquete_desafio_2.funciones import *

lineas = ["linea 1", "linea 2", "linea 3"]
coches = ["coche 1", "coche 2", "coche 3", "coche 4", "coche 5"]

print("Menú de opciones:")
print("Opción 1: Cargar planilla de recaudaciones.")
print("Opción 2: Mostrar la recaudación de cada coche y línea.")
print("Opción 3: Calcular y mostrar la recaudación por línea.")
print("Opción 4: Calcular y mostrar la recaudación por coche.")
print("Opción 5: Calcular y mostrar la recaudación total.")
print("Opción 6: Salir del programa")

matriz_legajos=[[42,65,24,57,76],[86,32,74,87,23],[85,36,45,75,67]]
matriz_recaudacion = inicializar_matriz(3,5)

menu = True

while menu == True:
    opcion = int(input("Ingrese una opción: "))

    match opcion:
        case 1:
            print("Opción 1: Cargar planilla de recaudaciones.")
            chofer = validar_legajo(int(input("Bienvenido/a. Ingrese número de legajo: ")))
            print(f"Número de legajo del chofer: {chofer}")
            print("Buscamos número de legajo en la matriz de legajos")
            if buscar_legajo(matriz_legajos, chofer) == False:
                print("El legajo no corresponde a un chofer.")
            else:
                print("El legajo existe y corresponde a un chofer")
                print("Comienza la carga de recaudaciones.")
                matriz_recaudacion = carga_recaudaciones(matriz_recaudacion, lineas, coches)
        case 2:
            print("Opción 2: Mostrar la recaudación de cada coche y línea.")
            mostrar_matriz(matriz_recaudacion)
        case 3:
            print("Opción 3: Calcular y mostrar la recaudación por línea.")
            recaudacion_lineas = sumar_filas_columnas(matriz_recaudacion, "Filas")
            for i in range(len(lineas)):
                print(f"{lineas[i]} ha recaudado ${recaudacion_lineas[i]}")
        case 4:
            print("Opción 4: Calcular y mostrar la recaudación por coche.")
            recaudacion_coches = sumar_filas_columnas(matriz_recaudacion, "Columnas")
            for i in range(len(coches)):
                print(f"{coches[i]} ha recaudado ${recaudacion_coches[i]}")
        case 5:
            print("Opción 5: Calcular y mostrar la recaudación total.")
            recudacion_total = calcular_recaudacion_total(matriz_recaudacion)
            print(f"El total general de todas las recaudaciones registradas es de ${recudacion_total}")
        case 6: 
            print("Opción 6: Salir del programa.")
            menu = False
