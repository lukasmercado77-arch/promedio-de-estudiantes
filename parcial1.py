categoria= input("Ingrese la categoria,A,B,C:").upper()
compra=float(input("ingrese el valor del monto: $"))
if compra < 0:
    print("El valor de la compra no es valido")
elif categoria == "A":
   if compra > 1000000:
      porcentaje = 20
   else:
      porcentaje = 10

elif categoria == "B":
   if compra > 100000:
      porcentaje = 15
   else:
      porcentaje = 5

elif categoria == "C":
   porcentaje = 5
else:
   porcentaje = 0
   print("categoria no valida")

if compra >= 0 and categoria in ["A","B","C"]:
   descuento = compra * porcentaje/100
   total = compra - descuento

print("Categoria:", categoria)
print("Porcentaje de descuento:", porcentaje, "%")
print("Dinero descontado: $", descuento)
print("Total a pagar:",total)
