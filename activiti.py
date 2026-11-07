import random
intentos=3
numero_aleatorio = random.randint(1,100)
numero_usuario = int(input("ingrese un numero del 1 al 100 :"))
while numero_usuario !=numero_aleatorio:
      print("tines 3 intentos:")
      
      numero_usuario=int(input("ingrese otro numero:"))
      print("numero incorrecto")
if numero_usuario == numero_aleatorio:
    print("¡felicidades adivinaste el numero.!")
else:
    print("no es el numero")
    print("el numero era.", numero_aleatorio)