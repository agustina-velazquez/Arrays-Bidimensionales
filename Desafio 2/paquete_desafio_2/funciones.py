

#las filas de la matriz serán las lineas y los coches las columnas

def validar_legajo(numero: int)->int:
    '''Valida que el numero de legajo sea un entero positivo
    '''
    if type(numero) != int:
        print("El número debe ser un entero")

    while numero < 0:
        numero = int(input("El legajo debe ser un número positivo: "))
    
    return numero



def inicializar_matriz(filas: int, columnas: int, valor: int=0)->list:
    '''Genera una matriz con la cantidad de filas y columnas dadas como parámetro. 
    Todos sus elementos tienen el valor del parámetro opcional
    '''
    matriz = []

    for i in range(filas):
        fila = [valor]*columnas
        matriz += [fila]

    return matriz    

def carga_legajos(matriz: list)-> list:
    '''Recibe una matriz y la carga secuencialmente, validando que los valores cargados sean positivos
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            legajo = validar_legajo(int(input("Ingrese número de legajo: ")))
            matriz[i][j] = legajo

    return matriz

def mostrar_matriz(matriz: list)->None:
    '''Recibe una matriz y la muestra por consol. No retorna nada
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " ")

        print(" ")

def buscar_legajo(matriz: list, legajo: int)->bool:
    '''Recibe una matriz y un número de legajo como parámetros.
    Si el legajo se encuentra en la matriz de legajos retorna True, caso contrario retorna False
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == legajo:
                return True
            
    return False


def buscar_lista(lista: list, elemento: str)-> int:
    '''Recibe una lista y un elemento como parámetros, en caso de que el elemento se encuentre
    en la lista. retorna el indice en el que se encuentra. Caso contrario no retorna nada.
    '''
    for i in range(len(lista)):
        if elemento == lista[i]:
            return i

def carga_recaudaciones(matriz: list, lineas: list, coches: list)->list:
    '''Recibe una matriz, y dos listas como parámetros que son las etiquetas de la matriz. 
    Carga la matriz recibida distributivamente/aleatoriamente 
    '''
    seguir_cargando = "Si"

    while seguir_cargando == "Si":
        linea = input("Ingrese la línea del viaje: ")
        coche = input("Ingrese el coche del viaje: ")
        recaudacion = int(input("Ingrese el monto de la recaudación: "))

        fila = buscar_lista(lineas, linea)
        columna = buscar_lista(coches, coche)
        matriz[fila][columna] += recaudacion

        seguir_cargando = input("¿Desea seguir cargando recaudaciones? Si/No: ")

    return matriz

def sumar_filas_columnas(matriz: list, lugar: str)->list:
    '''Recibe una matriz y un lugar como parámetros. El lugar indica si se sumará por filas o columanas
    Retorna una lista, donde sus elementos son la suma de cada fila o cada columna.
    '''
    lista_suma = []

    if lugar == "Filas":
        for i in range(len(matriz)):
            suma = 0
            for j in range(len(matriz[i])):
                suma += matriz[i][j]
            lista_suma += [suma]
        
    else:
        columnas = matriz[0] #es la primera fila que tiene como tamaño el numero de columnas
        for i in range(len(columnas)): #5 iter
            suma = 0
            for j in range(len(matriz)): #3 iter
                suma += matriz[j][i]
            lista_suma += [suma]

    return lista_suma

def calcular_recaudacion_total(matriz: list)->int:
    '''Recibe una matriz como parámetro y retorna la suma de todos sus elementos
    '''
    total = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total += matriz[i][j]
    
    return total



