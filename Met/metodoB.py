# -0.5 * in1**2 * 2.5 * in1 * 4.5
# −2  −1

in1 = float(input("Ingresa el primer intervalo: "))
in2 = float(input("Ingresa el segundo intervalo: "))

a = float(input("Ingresa el valor de a (de x): "))
b = float(input("Ingresa el valor de b (de x): "))
c = float(input("Ingresa el valor de c: "))

formato = []

for i in range(5):
    val1 = a * in1**2 + b * in1 + c
    val2 = a * in2**2 + b * in2 + c

    medio = (in1 + in2) / 2
    intervalo = a * medio**2 + b * medio + c

    if val1 * intervalo < 0: 
        valorAnterior = in1
        valorActual = medio
    else: 
        valorAnterior = in2
        valorActual = medio

    if i > 0:
        error = abs((valorActual - valorAnterior) / valorActual) * 100
    else:
        error = '' 

    formato.append([in1, in2, medio, intervalo, valorActual, valorAnterior, error])

    in1 = valorAnterior
    in2 = valorActual

for x in formato:
    print(x)

print("El programa ha terminado.")
