funcion = input("Ingresa la función f(x) en términos de x como se muestra en el ejemplo (ej. 5*x**3 - 5*x**2 + 6*x - 2): ")

in1 = float(input("Ingresa el primer intervalo (a): "))
in2 = float(input("Ingresa el segundo intervalo (b): "))
iteraciones = int(input("Ingresa el número de iteraciones: "))

resultados = []

def f(x):
    return eval(funcion)

for i in range(iteraciones):
    fa = f(in1)
    fb = f(in2)
    
    c = in2 - (fb * (in1 - in2)) / (fa - fb)
    fc = f(c)
    
    if i > 0:
        error = abs((c - c_anterior) / c) * 100
    else:
        error = None  
    

    resultados.append([
        i+1, 
        round(in1, 4), 
        round(in2, 4), 
        round(c, 4), 
        round(fa, 4), 
        round(fb, 4), 
        round(fc, 4), 
        round(error, 4) if error is not None else '-'
    ])
    
    if fa * fc < 0:
        in2 = c
    else:
        in1 = c
    
    c_anterior = c

print("Iteración |   a    |   b    |    c    |   f(a)   |   f(b)   |   f(c)   |  Error %")
for resultado in resultados:
    print(resultado)
