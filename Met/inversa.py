def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)
    print()

def determinante_3x3(matriz):
    det = (matriz[0][0] * (matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1]) -
           matriz[0][1] * (matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0]) +
           matriz[0][2] * (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0]))
    return det

def matriz_cofactores(matriz):
    cofactores = [[0 for _ in range(3)] for _ in range(3)]
    
    cofactores[0][0] = matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1]
    cofactores[0][1] = -(matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0])
    cofactores[0][2] = matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0]
    
    cofactores[1][0] = -(matriz[0][1] * matriz[2][2] - matriz[0][2] * matriz[2][1])
    cofactores[1][1] = matriz[0][0] * matriz[2][2] - matriz[0][2] * matriz[2][0]
    cofactores[1][2] = -(matriz[0][0] * matriz[2][1] - matriz[0][1] * matriz[2][0])
    
    cofactores[2][0] = matriz[0][1] * matriz[1][2] - matriz[0][2] * matriz[1][1]
    cofactores[2][1] = -(matriz[0][0] * matriz[1][2] - matriz[0][2] * matriz[1][0])
    cofactores[2][2] = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    return cofactores

def transponer_matriz(matriz):
    transpuesta = [[matriz[j][i] for j in range(3)] for i in range(3)]
    return transpuesta

def multiplicar_matriz_por_escalar(matriz, escalar):
    return [[escalar * matriz[i][j] for j in range(3)] for i in range(3)]

def calcular_inversa(matriz):
    det = determinante_3x3(matriz)
    if det == 0:
        print("La matriz no tiene inversa.")
        return None
    else:
        cofactores = matriz_cofactores(matriz)
        adjunta = transponer_matriz(cofactores)
        inversa = multiplicar_matriz_por_escalar(adjunta, 1/det)
        return inversa

def ingresar_sistema():
    n = 3 
    matriz = []
    resultados = []

    print("Ingrese los coeficientes de la matriz:")
    for i in range(n):
        fila = []
        for j in range(n):
            coef = float(input(f"Ingrese el coeficiente a[{i+1}][{j+1}]: "))
            fila.append(coef)
        matriz.append(fila)

    print("Ingrese los resultados de las ecuaciones:")
    for i in range(n):
        resultado = float(input(f"Ingrese el resultado de la ecuación {i+1}: "))
        resultados.append(resultado)

    print("\nMatriz de coeficientes:")
    imprimir_matriz(matriz)
    
    print("Vector de resultados:")
    imprimir_matriz([resultados])
    
    return matriz, resultados

def multiplicar_matriz_vector(matriz, vector):
    resultado = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            resultado[i] += matriz[i][j] * vector[j]
    return resultado

def resolver_por_matriz_inversa():
    matriz, resultados = ingresar_sistema()

    inversa = calcular_inversa(matriz)
    
    if inversa is not None:
        print("Matriz inversa:")
        imprimir_matriz(inversa)
        
        soluciones = multiplicar_matriz_vector(inversa, resultados)
        
        print("Soluciones:")
        imprimir_matriz([soluciones])

def menu():
    print("Seleccione el método para resolver el sistema de ecuaciones:")
    print("1. Matriz Inversa")
    
    opcion = int(input("Ingrese su opción (1): "))
    
    if opcion == 1:
        resolver_por_matriz_inversa()
    else:
        print("Opción no válida.")

menu()
