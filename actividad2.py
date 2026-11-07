numeros = [14, 25, 42, 31, 19, 8, 50, 73, 11, 22,23,28,23,15,1,2,5,7,8,30,77,100]

pares = []
impares = []

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        pares = pares + [numeros[i]]
    else:
        impares = impares + [numeros[i]]

print("Numeros pares:", pares)
print("Total de pares:", len(pares))

print("Numeros impares:", impares)
print("Total de impares:", len(impares))
