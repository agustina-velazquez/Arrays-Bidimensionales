from paquete_desafio_1.funciones import *

matriz = inicializar_matriz(3,3)

if validar_tamaño(matriz) == False:
    print("La matriz debe ser cuadrada")
else: 
    matriz = cargar_matriz(matriz)
            

cte_magica = calcular_cte_magica(len(matriz))

suma_filas = sumar_filas_columnas(matriz,"Fila")
suma_columnas = sumar_filas_columnas(matriz,"Columna")
suma_diagonal_ppal = sumar_diagonales(matriz, "principal")
suma_diagonal_sec = sumar_diagonales(matriz,"antidiagonal")

mostrar_matriz(matriz)
print(f"La constante mágica es {cte_magica}")
print(f"La suma de las filas es {suma_filas}")
print(f"La suma de las columnas es {suma_columnas}")
print(f"La suma de la diagonal principal es {suma_diagonal_ppal}")
print(f"La suma de la antidiagonal es {suma_diagonal_sec}")


verificacion(matriz, suma_filas, suma_columnas, suma_diagonal_ppal, suma_diagonal_sec, cte_magica)







