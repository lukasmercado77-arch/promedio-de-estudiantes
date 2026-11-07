
nombre=input("ingrese su nombre:")
nota1=float(input("primera nota:"))
nota2=float(input("segunda nota:"))
nota3=float(input("tercera nota:"))

calcular=(nota1+nota2+nota3) /3

print("Tu nombre es",nombre)
print("Tu promedio es",calcular)
 
nota= 20
if(nota>5 or nota<1):
  print("nota no puede ser mayor que 5")
elif(nota>= 3): 
  print("gano")
else:
 print("perdio")