def imprimir_matriz(matriz):
    for fila in matriz:
        print([round(elem, 2) for elem in fila]) 
    print()

def ingresar_datos():
    n = int(input("Ingrese la cantidad de puntos (al menos 3): "))
    x = []
    y = []
    
    print("Ingrese los valores de x y y para cada punto:")
    for i in range(n):
        xi = float(input(f"Ingrese x[{i+1}]: "))
        yi = float(input(f"Ingrese y[{i+1}]: "))
        x.append(xi)
        y.append(yi)
    
    return x, y

def calcular_regresion_cuadratica(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum([xi**2 for xi in x])
    sum_x3 = sum([xi**3 for xi in x])
    sum_x4 = sum([xi**4 for xi in x])
    sum_xy = sum([x[i] * y[i] for i in range(n)])
    sum_x2y = sum([x[i]**2 * y[i] for i in range(n)])

    matriz = [
        [n, sum_x, sum_x2],
        [sum_x, sum_x2, sum_x3],
        [sum_x2, sum_x3, sum_x4]
    ]
    
    resultados = [sum_y, sum_xy, sum_x2y]
    
    return matriz, resultados

def determinante_3x3(matriz):
    return (
        matriz[0][0] * (matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1])
        - matriz[0][1] * (matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0])
        + matriz[0][2] * (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0])
    )

def matriz_inversa_3x3(matriz):
    det = determinante_3x3(matriz)
    if det == 0:
        print("La matriz no tiene inversa.")
        return None
    else:
        adjunta = [
            [
                (matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1]) / det,
                -(matriz[0][1] * matriz[2][2] - matriz[0][2] * matriz[2][1]) / det,
                (matriz[0][1] * matriz[1][2] - matriz[0][2] * matriz[1][1]) / det
            ],
            [
                -(matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0]) / det,
                (matriz[0][0] * matriz[2][2] - matriz[0][2] * matriz[2][0]) / det,
                -(matriz[0][0] * matriz[1][2] - matriz[0][2] * matriz[1][0]) / det
            ],
            [
                (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0]) / det,
                -(matriz[0][0] * matriz[2][1] - matriz[0][1] * matriz[2][0]) / det,
                (matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]) / det
            ]
        ]
        return adjunta

def multiplicar_matriz_vector_3x3(matriz, vector):
    return [
        matriz[0][0] * vector[0] + matriz[0][1] * vector[1] + matriz[0][2] * vector[2],
        matriz[1][0] * vector[0] + matriz[1][1] * vector[1] + matriz[1][2] * vector[2],
        matriz[2][0] * vector[0] + matriz[2][1] * vector[1] + matriz[2][2] * vector[2]
    ]

def resolver_regresion_cuadratica():
    x, y = ingresar_datos()

    matriz, resultados = calcular_regresion_cuadratica(x, y)
    
    print("\nMatriz de coeficientes (A):")
    imprimir_matriz(matriz)
    
    print("Vector de resultados (b):")
    imprimir_matriz([resultados])

    inversa = matriz_inversa_3x3(matriz)
    
    if inversa is not None:
        print("Matriz inversa (A^-1):")
        imprimir_matriz(inversa)

        soluciones = multiplicar_matriz_vector_3x3(inversa, resultados)

        a = round(soluciones[2], 2)  
        b = round(soluciones[1], 2)  
        c = round(soluciones[0], 2)  

        print(f"\nEcuación de la curva: y = {a}x^2 + {b}x + {c}")
        return a, b, c

def menu():
    print("Seleccione una opción:")
    print("1. Regresión Cuadrática")
    
    opcion = int(input("Ingrese su opción (1): "))
    
    if opcion == 1:
        resolver_regresion_cuadratica()
    else:
        print("Opción no válida.")

menu()