n = int(input("¿Cuántos términos de Fibonacci desea mostrar? "))

a = 0
b = 1

if n <= 0:
    print("Ingrese un número entero positivo")
else:
    for i in range(n):
        print(a, end=" ")

        siguiente = a + b
        a = b
        b = siguiente

    print()