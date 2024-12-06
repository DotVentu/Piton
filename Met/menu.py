import os
import subprocess

def menu():
    ruta_base = os.path.dirname(os.path.abspath(__file__))

    while True:
        print("\n--- Menú Principal ---")
        print("1. Método Bisección")
        print("2. Método Falsa posición")
        print("3. Método Newton-Raphson")
        print("4. Método de la Secante")
        print("5. Método Ecuaciones LIneales")
        print("6. Método Ecuaciones LIneales Gauss-Jordan")
        print("7. Método Ecuaciones LIneales Matriz Inversa 3x3")
        print("8. Método Regresión Lineal")
        print("9. Método Regresión Cuadrática")
        print("10. Método Regla de los rectángulos")
        print("11. Método Newton - Cotes")
        print("12. Método Simpson")
        print("13. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ruta_metodo = os.path.join(ruta_base, "metodoB.py")
            subprocess.run(["python", ruta_metodo])
        elif opcion == "2":
            ruta_metodo = os.path.join(ruta_base, "MetodoFa.py")
            subprocess.run(["python", ruta_metodo])
        elif opcion == "3":
            ruta_metodo = os.path.join(ruta_base, "metodoN.py")
            subprocess.run(["python", ruta_metodo])
        elif opcion == "4":
            ruta_metodo = os.path.join(ruta_base, "MetodoS.py")
            subprocess.run(["python", ruta_metodo])
        elif opcion == "5":
            ruta_metodo = os.path.join(ruta_base, "EcuacionesLineale.py")
            subprocess.run(["python", ruta_metodo])
        elif opcion == "6":
            ruta_metodo = os.path.join(ruta_base, "Gaus.py")
            subprocess.run(["python", ruta_metodo])
        elif opcion == "7":
            ruta_metodo = os.path.join(ruta_base, "inversa.py")
            subprocess.run(["python", ruta_metodo])
        elif opcion == "8":
            ruta_metodo = os.path.join(ruta_base, "lineal.py")
            subprocess.run(["python", ruta_metodo])
        elif opcion == "9":
            ruta_metodo = os.path.join(ruta_base, "cuadratica.py")
            subprocess.run(["python", ruta_metodo])
        elif opcion == "10":
            ruta_metodo = os.path.join(ruta_base, "Riemann.py")
            subprocess.run(["python", ruta_metodo])
        elif opcion == "11":
            ruta_metodo = os.path.join(ruta_base, "Newton.py")
            subprocess.run(["python", ruta_metodo])
        elif opcion == "12":
            ruta_metodo = os.path.join(ruta_base, "simpson.py")
            subprocess.run(["python", ruta_metodo])
        elif opcion == "13":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

menu()
