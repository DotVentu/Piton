import math

def imprimir_resultados(resultados):
    print("Áreas de cada subintervalo:")
    for i, valor in enumerate(resultados, start=1):
        print(f"Subintervalo {i}: {valor:.4f}")
    print()

def calcular_suma_riemann(funcion_str, a, b, n, metodo):
    ancho = (b - a) / n
    suma = 0
    resultados = []

    for i in range(n):
        if metodo == "puntos_muestra":
            x = a + i * ancho
        elif metodo == "punto_medio":
            x = a + (i + 0.5) * ancho
        else:
            raise ValueError("Método no válido")
        
        fx = eval(funcion_str)
        area = fx * ancho
        suma += area
        resultados.append(area)

    imprimir_resultados(resultados)
    return suma

def ingresar_datos():
    funcion_str = input("Ingrese la función f(x) en términos de x (por ejemplo, '25 - x**2'): ")
    a = float(input("Ingrese el límite inferior del intervalo: "))
    b = float(input("Ingrese el límite superior del intervalo: "))
    n = int(input("Ingrese el número de subintervalos: "))
    print("Métodos disponibles:")
    print("1. Punto de muestra (extremo izquierdo)")
    print("2. Punto medio")
    metodo_opcion = int(input("Seleccione el método (1 o 2): "))
    metodo = "puntos_muestra" if metodo_opcion == 1 else "punto_medio"
    return funcion_str, a, b, n, metodo

def resolver_problema():
    funcion_str, a, b, n, metodo = ingresar_datos()
    
    area = calcular_suma_riemann(funcion_str, a, b, n, metodo)
    print(f"\nÁrea estimada bajo la curva: {area:.4f}")

resolver_problema()
