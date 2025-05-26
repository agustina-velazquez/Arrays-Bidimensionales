def validar_numero(numero: int, tamaño: int)->int:
    '''recibe un numero y el tamaño de la matriz como parámetros. Evalua si esta dentro del rango y,
    en caso de no estarlo, pide al usuario otro valor hasta que el mismo se encuentre en el rango
    y lo retorna
    '''
    if type(numero) != int:
        print("El número debe ser un entero")
    while numero < 0 or numero > tamaño**2:
        numero = int(input("Fuera de rango. Ingrese un numero valido: "))

    return numero
    
def validar_tamaño(matriz: list)->bool:
    '''Recibe una matriz como parámetro. Si el numero de filas es igual al de columnas, quiere decir que es una matriz cuadrada.
    Caso contrario retorna False
    '''
    filas = len(matriz)
    columnas = len(matriz[1])
    if filas == columnas:
        return True
    else:
        return False
    
def inicializar_matriz(filas: int, columnas: int, valor: int = 0)-> list:
    '''Recibe el numero de filas y columnas, retorna una matriz con esas dimensiones y con todos sus valores iguales al
    parámetro opcional
    '''
    matriz = []
    for i in range(filas):
        fila = [valor] * columnas
        matriz += [fila]
    
    return matriz

def cargar_matriz(matriz: list)->list:
    '''Recibe una matriz como parámetro, la carga secuencialmente, validando que los valores cargados esten dentro del rango
    pedido
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            valor = int(input(f"Ingrese valor para la fila {i}, columna {j}: "))
            valor = validar_numero(valor, len(matriz))
            matriz[i][j] = valor

    return matriz

def calcular_cte_magica(n: int)->int:
    '''Recibe el tamaño de la matriz como parámetro y calcula la constante mágica de la misma
    '''
    cte_magica = (n*(n**2+1))/2
    return cte_magica

def sumar_filas_columnas(matriz: list, lugar: str)-> list:
    '''Recibe una matriz, un lugar: fila o columna. Devuelve una lista 
    donde cada elemento es la suma de cada fila o columna
    '''
    
    lista_suma = []

    if lugar == "Fila":
        for i in range(len(matriz)):
            suma = 0
            for j in range(len(matriz[i])):
                suma += matriz[i][j]

            lista_suma += [suma]
    else:
        columnas = len(matriz[0])
        for i in range(columnas): 
            suma = 0
            for j in range(len(matriz)): 
                suma += matriz[j][i]

            lista_suma += [suma]

    return lista_suma


def sumar_diagonales(matriz: list, diagonal: str)-> int:
    '''Recibe una matriz y una diagonal como parámetros. Calcula la suma de esta última.
    '''
    suma = 0

    if diagonal == "principal":
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if i == j:
                    suma += matriz[i][j]
                    break
    else:
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if i+j == len(matriz)-1:
                    suma += matriz[i][j]
                    break
    return suma

def verificacion(matriz: int, filas: list, columnas:list, diagonal_1:int, diagonal_2:int, cte:int)-> bool:
    '''Recibe una matriz, la suma de sus filas, la suma de sus columnas, la suma de su diagonal y antidiagonal. 
    Compara cada una de esas sumas con la constante mágica y retorna True en caso de que todas las sumas sean iguales a la constante
    mágica. Retorna False en caso contrario
    '''
    for i in range(len(matriz)):
        if filas[i] == cte and columnas[i] == cte and diagonal_1 == cte and diagonal_2 == cte:
            print("La matriz es un cuadrado magico")
            return True
        else: 
            print("La matriz no es un cuadrado magico")
            return False
        
def mostrar_matriz(matriz: list)->None:
    '''Muestra una matriz de forma clara y organizada. No retorna nada
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " ")
        print(" ")

