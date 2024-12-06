def determinante_2x2(matriz):
    return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

def determinante_3x3(matriz):
    return (matriz[0][0] * (matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1])
          - matriz[0][1] * (matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0])
          + matriz[0][2] * (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0]))

def metodo_de_cramer_2x2(A, B):
    det_A = determinante_2x2(A)
    
    if det_A == 0:
        raise ValueError("El sistema no tiene solución única (determinante de A es 0).")
    
    A_x = [[B[0], A[0][1]], [B[1], A[1][1]]]
    A_y = [[A[0][0], B[0]], [A[1][0], B[1]]]
    
    det_x = determinante_2x2(A_x)
    det_y = determinante_2x2(A_y)
    
    x = det_x / det_A
    y = det_y / det_A
    
    return x, y

def metodo_de_cramer_3x3(A, B):
    det_A = determinante_3x3(A)
    
    if det_A == 0:
        raise ValueError("El sistema no tiene solución única (determinante de A es 0).")
    
    A_x = [[B[0], A[0][1], A[0][2]], [B[1], A[1][1], A[1][2]], [B[2], A[2][1], A[2][2]]]
    A_y = [[A[0][0], B[0], A[0][2]], [A[1][0], B[1], A[1][2]], [A[2][0], B[2], A[2][2]]]
    A_z = [[A[0][0], A[0][1], B[0]], [A[1][0], A[1][1], B[1]], [A[2][0], A[2][1], B[2]]]
    
    det_x = determinante_3x3(A_x)
    det_y = determinante_3x3(A_y)
    det_z = determinante_3x3(A_z)
    
    x = det_x / det_A
    y = det_y / det_A
    z = det_z / det_A
    
    return x, y, z

def sistema_cramer():
    n = int(input("¿Cuántas ecuaciones tiene el sistema (2 o 3)? "))
    
    if n == 2:
        print("Sistema de ecuaciones 2x2:")
        print("Ecuación 1: a1*x + b1*y = c1")
        print("Ecuación 2: a2*x + b2*y = c2")
        
        a1 = float(input("\nIngrese el valor de a1 (coeficiente de x en la primera ecuación): "))
        b1 = float(input("Ingrese el valor de b1 (coeficiente de y en la primera ecuación): "))
        c1 = float(input("Ingrese el valor de c1 (resultado de la primera ecuación): "))
        
        a2 = float(input("\nIngrese el valor de a2 (coeficiente de x en la segunda ecuación): "))
        b2 = float(input("Ingrese el valor de b2 (coeficiente de y en la segunda ecuación): "))
        c2 = float(input("Ingrese el valor de c2 (resultado de la segunda ecuación): "))
        
        A = [
            [a1, b1],
            [a2, b2]
        ]
        
        B = [c1, c2]
        
        print("\nMatriz A (coeficientes):")
        for fila in A:
            print(fila)
        
        print("\nMatriz B (resultados):")
        print(B)
        
        try:
            x, y = metodo_de_cramer_2x2(A, B)
            print(f"\nSolución: x = {x}, y = {y}")
        except ValueError as e:
            print(e)
    
    elif n == 3:
        print("Sistema de ecuaciones 3x3:")
        print("Ecuación 1: a1*x + b1*y + c1*z = d1")
        print("Ecuación 2: a2*x + b2*y + c2*z = d2")
        print("Ecuación 3: a3*x + b3*y + c3*z = d3")
        
        a1 = float(input("\nIngrese el valor de a1 (coeficiente de x en la primera ecuación): "))
        b1 = float(input("Ingrese el valor de b1 (coeficiente de y en la primera ecuación): "))
        c1 = float(input("Ingrese el valor de c1 (coeficiente de z en la primera ecuación): "))
        d1 = float(input("Ingrese el valor de d1 (resultado de la primera ecuación): "))
        
        a2 = float(input("\nIngrese el valor de a2 (coeficiente de x en la segunda ecuación): "))
        b2 = float(input("Ingrese el valor de b2 (coeficiente de y en la segunda ecuación): "))
        c2 = float(input("Ingrese el valor de c2 (coeficiente de z en la segunda ecuación): "))
        d2 = float(input("Ingrese el valor de d2 (resultado de la segunda ecuación): "))
        
        a3 = float(input("\nIngrese el valor de a3 (coeficiente de x en la tercera ecuación): "))
        b3 = float(input("Ingrese el valor de b3 (coeficiente de y en la tercera ecuación): "))
        c3 = float(input("Ingrese el valor de c3 (coeficiente de z en la tercera ecuación): "))
        d3 = float(input("Ingrese el valor de d3 (resultado de la tercera ecuación): "))
        

        A = [
            [a1, b1, c1],
            [a2, b2, c2],
            [a3, b3, c3]
        ]
        
        B = [d1, d2, d3]
        
        print("\nMatriz A (coeficientes):")
        for fila in A:
            print(fila)
        
        print("\nMatriz B (resultados):")
        print(B)
        
        try:
            x, y, z = metodo_de_cramer_3x3(A, B)
            print(f"\nSolución: x = {x}, y = {y}, z = {z}")
        except ValueError as e:
            print(e)
    else:
        print("Este programa solo resuelve sistemas de 2x2 o 3x3.")

sistema_cramer()
