def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)
    print()

def eliminacion_gaussiana(matriz):
    n = len(matriz)
    for i in range(n):
        divisor = matriz[i][i]
        for j in range(i, n + 1):
            matriz[i][j] /= divisor

        for k in range(i + 1, n):
            factor = matriz[k][i]
            for j in range(i, n + 1):
                matriz[k][j] -= factor * matriz[i][j]

def sustitucion_regresiva(matriz):
    n = len(matriz)
    soluciones = [0] * n
    for i in range(n - 1, -1, -1):
        soluciones[i] = matriz[i][n]
        for j in range(i + 1, n):
            soluciones[i] -= matriz[i][j] * soluciones[j]
    return soluciones

def gauss_jordan(matriz):
    n = len(matriz)
    for i in range(n):

        divisor = matriz[i][i]
        for j in range(n + 1):
            matriz[i][j] /= divisor

        for k in range(n):
            if k != i:
                factor = matriz[k][i]
                for j in range(n + 1):
                    matriz[k][j] -= factor * matriz[i][j]

def ingresar_sistema():
    n = int(input("Ingrese el número de ecuaciones (2 o 3): "))
    matriz = []
    
    for i in range(n):
        fila = []
        for j in range(n):
            coef = float(input(f"Ingrese el coeficiente a[{i+1}][{j+1}]: "))
            fila.append(coef)
        resultado = float(input(f"Ingrese el resultado de la ecuación {i+1}: "))
        fila.append(resultado)
        matriz.append(fila)
    
    print("\nMatriz aumentada:")
    imprimir_matriz(matriz)
    
    return matriz

def resolver_por_gauss():
    matriz = ingresar_sistema()
    eliminacion_gaussiana(matriz)
    print("Matriz triangular superior:")
    imprimir_matriz(matriz)
    soluciones = sustitucion_regresiva(matriz)
    print("Soluciones:", soluciones)

def resolver_por_gauss_jordan():
    matriz = ingresar_sistema()
    gauss_jordan(matriz)
    print("Matriz reducida a identidad:")
    imprimir_matriz(matriz)
    soluciones = [fila[-1] for fila in matriz]
    print("Soluciones:", soluciones)

def menu():
    print("Seleccione el método para resolver el sistema de ecuaciones:")
    print("1. Eliminación de Gauss")
    print("2. Gauss-Jordan")
    
    opcion = int(input("Ingrese su opción (1 o 2): "))
    
    if opcion == 1:
        resolver_por_gauss()
    elif opcion == 2:
        resolver_por_gauss_jordan()
    else:
        print("Opción no válida.")

menu()
