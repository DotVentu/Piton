def imprimir_matriz(matriz):
    for fila in matriz:
        print([round(elem, 2) for elem in fila])  # Redondear a 2 decimales
    print()

def ingresar_datos():
    # Ingresar los valores de x y y
    n = int(input("Ingrese la cantidad de puntos: "))
    x = []
    y = []
    
    print("Ingrese los valores de x y y para cada punto:")
    for i in range(n):
        xi = float(input(f"Ingrese x[{i+1}]: "))
        yi = float(input(f"Ingrese y[{i+1}]: "))
        x.append(xi)
        y.append(yi)
    
    return x, y

def calcular_regresion_lineal(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum([xi**2 for xi in x])
    sum_xy = sum([x[i] * y[i] for i in range(n)])

    # Matriz de coeficientes (A)
    matriz = [
        [n, sum_x],    
        [sum_x, sum_x2]
    ]
    
    # Vector de resultados (b)
    resultados = [sum_y, sum_xy]
    
    return matriz, resultados

def determinante_2x2(matriz):
    return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

def matriz_inversa_2x2(matriz):
    det = determinante_2x2(matriz)
    if det == 0:
        print("La matriz no tiene inversa.")
        return None
    else:
        inversa = [[matriz[1][1] / det, -matriz[0][1] / det],
                   [-matriz[1][0] / det, matriz[0][0] / det]]
        return inversa

def multiplicar_matriz_vector_2x2(matriz, vector):
    return [
        matriz[0][0] * vector[0] + matriz[0][1] * vector[1],
        matriz[1][0] * vector[0] + matriz[1][1] * vector[1]
    ]

def resolver_regresion_lineal():
    x, y = ingresar_datos()

    # Calcular la matriz de coeficientes y el vector de resultados
    matriz, resultados = calcular_regresion_lineal(x, y)
    
    print("\nMatriz de coeficientes (A):")
    imprimir_matriz(matriz)
    
    print("Vector de resultados (b):")
    imprimir_matriz([resultados])

    # Calcular la inversa de la matriz A
    inversa = matriz_inversa_2x2(matriz)
    
    if inversa is not None:
        print("Matriz inversa (A^-1):")
        imprimir_matriz(inversa)

        # Resolver el sistema A * [m, b] = b
        soluciones = multiplicar_matriz_vector_2x2(inversa, resultados)

        # Redondear la pendiente y la intersección a 2 decimales
        m = round(soluciones[1], 2)  # Pendiente
        b = round(soluciones[0], 2)  # Intersección

        print(f"\nEcuación de la recta: y = {m}x + {b}")
        return m, b

def menu():
    print("Seleccione una opción:")
    print("1. Regresión Lineal")
    
    opcion = int(input("Ingrese su opción (1): "))
    
    if opcion == 1:
        resolver_regresion_lineal()
    else:
        print("Opción no válida.")

menu()
