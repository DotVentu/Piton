def imprimir_resultados(resultados):
    print("Áreas de cada subintervalo:")
    for i, valor in enumerate(resultados, start=1):
        print(f"Subintervalo {i}: {valor:.4f}")
    print()

def calcular_area_trapecios(funcion_str, a, b, n):
    ancho = (b - a) / n
    suma = 0
    resultados = []

    for i in range(n):
        x_i = a + i * ancho
        x_i1 = a + (i + 1) * ancho
        fx_i = eval(funcion_str.replace("x", str(x_i)))
        fx_i1 = eval(funcion_str.replace("x", str(x_i1)))
        area_trapecio = (fx_i + fx_i1) * ancho / 2
        suma += area_trapecio
        resultados.append(area_trapecio)

    imprimir_resultados(resultados)
    return suma

def ingresar_datos():
    funcion_str = input("Ingrese la función f(x) en términos de x (por ejemplo, '25 - x**2'): ")
    a = float(input("Ingrese el límite inferior del intervalo: "))
    b = float(input("Ingrese el límite superior del intervalo: "))
    n = int(input("Ingrese el número de subintervalos: "))
    return funcion_str, a, b, n

def resolver_problema():
    funcion_str, a, b, n = ingresar_datos()
    
    print(f"\nCálculo con {n} divisiones:")
    area = calcular_area_trapecios(funcion_str, a, b, n)
    print(f"Área estimada con {n} divisiones: {area:.4f}\n")

    n_doble = n * 2
    print(f"\nCálculo con {n_doble} divisiones:")
    area_doble = calcular_area_trapecios(funcion_str, a, b, n_doble)
    print(f"Área estimada con {n_doble} divisiones: {area_doble:.4f}\n")

resolver_problema()
