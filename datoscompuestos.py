

#creando una lista  (se puede modificar)
lista =["Lucas madera"," soy Lucas",True,1.76]

#creando una tupla (no se puede modificar)
tupla = ("Lucas madera","Soy Lucas",True,1.76)

#esto es valido
lista[3]="maquinanola"

#esto No es valido
#Trupla[3]"maquinanola"

#crenado un conjunto (set) no almacena datos por indice, no almacena datos duplicados
conjunto={"Lucas madera", "Soy Lucas",True,1.76}
#print[3] -> no puede acceder al elemento


#crenado un diccionario (dict) (la estructura es key: value y separe con comas)
diccionario ={
    'nombre' :"Lucas madera",
    'canal': "soy lucas",
    'esta_emocionado':True,
    'Altura': 1.76,
    'datos_duplicados': "soy dalto"
}
print(diccionario['Altura'])
