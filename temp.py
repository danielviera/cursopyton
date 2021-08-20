# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
lugar=input("Ingrese su direccion: ")
edad=int(input("Ingrese su edad: "))
espacio=" "

print("Su nombre:"+espacio+nombre+espacio+apellido)
print("Su domicilio:"+espacio+lugar)
if edad>=1 and edad<=18:
    print("Usted es un niño y su edad es:",edad)
elif edad>=18 and edad<=59:
    print("Usted es persona adulta y su edad es:",edad)
elif edad>=60:
    print("Usted es persona de tercera eddad y su edad es:",edad)
else:
    print("valor de edad es incorrecto")"""

"""lista1=[]
lista2=[]
lista=["R1","R2","S3","S4","R5"]
for i in lista:
    if "R" in i:
        print(i)
        lista2.append(i)
    elif "S" in i:
        lista1.append(i)

print(lista1)
print(lista1)"""

"""for i in range(10,0,-1):
    print(i, end=" ")"""

"""x=input("Ingrese un número: ")
x=int(x)
y=1
while y<=x:
    print(y)
    y+=1"""
    
    
"""x=input("Ingrese un número: ")
x=int(x)
y=1
while True:
    print(y)
    y+=1
    if y>x:
        break"""
        
        
"""while True:
    x=input("Ingrese un número: ")
    if x == 'q' or x =='quit':
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break"""

"""def saludo(nombre1, nombre2):
    print("Hola,", nombre1)
    print("Hola,", nombre2)

texto1=input("Ingrese un nombre1: ")
texto2=input("Ingrese un nombre1: ")
saludo(texto1,texto2)"""



"""def listafun(lista):
    for i in lista:
        print("hola!", i)
    print("\n"*2)
    
listafun(["Daniel"])
listafun(["Daniel", "Benjamin"])
listafun(["Daniel", "Benjamin", "Viera"])"""

"""def crearlista(n):
    lista=[]
    for i in range(n):
        lista.append(i)
    return lista

resultado=crearlista(5)
print(resultado)"""


def suma(*a):
    print("\nTipo de dato", type(a))
    sum=0
    for n in a:
        sum+=n
    print("Suma:", sum)

suma(3)
suma(4)
suma(4,5)





























