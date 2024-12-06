def imprimir_resultados(resultados):
    print("Áreas de cada segmento:")
    for i, valor in enumerate(resultados, start=1):
        print(f"Segmento {i}: {valor:.4f}")
    print()

def calcular_area_simpson_13(funcion_str, a, b, n):
    if n % 2 != 0:
        raise ValueError("El número de subintervalos (n) debe ser par para Simpson 1/3.")
    
    h = (b - a) / n
    suma = 0
    resultados = []
    
    for i in range(n + 1):
        x_i = a + i * h
        fx_i = eval(funcion_str.replace("x", str(x_i)))
        if i == 0 or i == n:
            suma += fx_i
        elif i % 2 == 0:
            suma += 2 * fx_i
        else:
            suma += 4 * fx_i
        resultados.append(fx_i)
    
    area = (h / 3) * suma
    imprimir_resultados(resultados)
    return area

def calcular_area_simpson_38(funcion_str, a, b, n):
    if n % 3 != 0:
        raise ValueError("El número de subintervalos (n) debe ser múltiplo de 3 para Simpson 3/8.")
    
    h = (b - a) / n
    suma = 0
    resultados = []
    
    for i in range(n + 1):
        x_i = a + i * h
        fx_i = eval(funcion_str.replace("x", str(x_i)))
        if i == 0 or i == n:
            suma += fx_i
        elif i % 3 == 0:
            suma += 2 * fx_i
        else:
            suma += 3 * fx_i
        resultados.append(fx_i)
    
    area = (3 * h / 8) * suma
    imprimir_resultados(resultados)
    return area

def ingresar_datos():
    funcion_str = input("Ingrese la función f(x) en términos de x (por ejemplo, '25 - x**2'): ")
    a = float(input("Ingrese el límite inferior del intervalo: "))
    b = float(input("Ingrese el límite superior del intervalo: "))
    metodo = int(input("Seleccione el método: 1 para Simpson 1/3, 2 para Simpson 3/8: "))
    n = int(input("Ingrese el número de subintervalos: "))
    return funcion_str, a, b, metodo, n

def resolver_problema():
    funcion_str, a, b, metodo, n = ingresar_datos()
    
    if metodo == 1:
        try:
            print("\nCálculo con Simpson 1/3:")
            area_13 = calcular_area_simpson_13(funcion_str, a, b, n)
            print(f"Área estimada con Simpson 1/3: {area_13:.4f}\n")
        except ValueError as e:
            print(e)
    elif metodo == 2:
        try:
            print("\nCálculo con Simpson 3/8:")
            area_38 = calcular_area_simpson_38(funcion_str, a, b, n)
            print(f"Área estimada con Simpson 3/8: {area_38:.4f}\n")
        except ValueError as e:
            print(e)
    else:
        print("Método no válido. Por favor, seleccione 1 o 2.")

resolver_problema()