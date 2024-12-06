# f(x) = −0.5x2 + 2.5x + 4.5.
# -0.5*x**2 + 2.5*x + 4.5

funcion = input("ingrese f(x) como se muestra en el ejemplo (ej. 5*x**3 - 5*x**2 + 6*x - 2):")

xi_1 = int(input("Ingrese el valor xi_1: "))
xi = int(input("Ingrese el valor xi: "))

iteraciones = int(input("ingrese la cantidad de iteraciones: "))

def f(x):
    return eval(funcion)

resultados = []

for i in range(iteraciones):
    
    fxi_1 = f(xi_1)
    fxi = f(xi)

    xim1 = xi - ((fxi*(xi_1 - xi)) / (fxi_1 - fxi))

    if i > 0:
        error = abs((xi - xim1) / xi) * 100
    else:
        error = None

    resultados.append([
     i + 1,
     round(xi_1, 4),
     round(fxi_1, 4),
     round(xi, 4),
     round(fxi, 4),
     round(xim1, 4),
     round(error, 4) if error is not None else '-'
    ])

    xi_1 =xi
    fxi_1 = fxi
    xi = xim1
    
print("Iteración |    xi_1     |    f(xi_1)    |   xi     |    f(xi)    |     xi+1     |   Error %")
for resultado in resultados:
  print(resultado)