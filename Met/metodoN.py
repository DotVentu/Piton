
funcion = input("Ingresa la función f(x) en términos de x como se muestra en el ejemplo (ej. 5*x**3 - 5*x**2 + 6*x - 2): ")

def derivada(f, x, h=0.0001):
  return (f(x + h) - f(x - h)) / (2 * h)

def f(x):
   return eval(funcion)

x0 = float(input("Ingresa el valor inicial (x0): "))
iteraciones = int(input("Ingresa el número de iteraciones: "))

resultados = []

for i in range(iteraciones):  
  fx0 = f(x0)
  dfx0 = derivada(f, x0)

  x1 = x0 - fx0 / dfx0

  if i > 0:
    error = abs((x1 - x0) / x1) * 100
  else:
    error = None

  resultados.append([
    i + 1,
    round(x0, 4),
    round(x1, 4),
    round(fx0, 4),
    round(dfx0, 4),
    round(error, 4) if error is not None else '-'
  ])

  x0 = x1

print("Iteración |  x0   |   x1    |   f(x0)  |  f'(x0)  |  Error %")
for resultado in resultados:
  print(resultado)
