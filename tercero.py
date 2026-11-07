nombre=input("ingrese nombre del cliente:")
compra=float(input("ingrese el valor de la compra"))

if compra > 100000:
     descuento=compra * 0.10
     total = compra -descuento
     print("cliente", nombre)
     print("descuento del 10%:", descuento)
     print("total a pagar", total) 
else:
    print("cliente:", nombre)
    print("no tiene descuento")
    print("total a pagar:", compra)