# x=6
# y=2
# print(f"{x} mas {y} es igual a {x+y}")
# print(f"{x} menos {y} es igual a {x-y}")
# print(f"{x} multiplicado {y} es igual a {x*y}")
# print(f"{x} dividido {y} es igual a {x/y}")
# z=7
# print(f"{z} dividido al piso {y} es igual a {z//y}")
# print(f"{z} modulo de {y} es igual a {z%y}")
# print(f"{x} elevado {y} es igual a {x**y}")
# print(f"La raiz cuadrada de {x} es igual a {x**0.5}")


#####################################################################

# print(round(90/7))
# valor=95.6666666
# print(round(valor,3))

#####################################################################

# Nombre=input("Escriba su nombre: ")
# Ventas=float(input("Cuánto has vendido este mes: "))
# Porcentaje= Ventas*0.13
# Redondeo= round(Porcentaje,2)
# print(f"{Nombre} tu comisión es: {Redondeo}")

#####################################################################

# mi_texto="Esto es una prueba"
# resultado=mi_texto[0]
# print(resultado)
# resultado= mi_texto.index("E")
# print(resultado)
# # resultado= mi_texto.index("j")
# # print(resultado)
# resultado= mi_texto.index("prueba")
# print(resultado)

#####################################################################

# texto="ABCDEFGHIJKLM"
# # fragmento=texto[0:3]
# # print(fragmento)
# # fragmento=texto[2:]
# # print(fragmento)
# # fragmento=texto[:3]
# # print(fragmento)
# # fragmento=texto[:]
# # print(fragmento)

# fragmento=texto[2:10:2]
# print(fragmento)

# fragmento=texto[::3]
# print(fragmento)

# fragmento=texto[::-1]
# print(fragmento)

#####################################################################

# Frase="Controlar la complejidad es la escncia de la programación"
# fragmento=Frase[0:9]
# print(fragmento)

# Frase2="Nunca confíes en un ordenador que no puedas lanzar por una ventana"
# fragmento=Frase2[9::3]
# print(fragmento)

# Frase3="Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
# fragmento=Frase3[::-1]
# print(fragmento)

#####################################################################

# texto="Este es un texto en Python"
# resultado=texto.upper()
# print(resultado)

# resultado=texto.lower()
# print(resultado)

# resultado=texto[3].upper()
# print(resultado)

# resultado=texto.split()
# print(resultado)

# resultado=texto.split("t")
# print(resultado)

#####################################################################

# palabra1="Aprender"
# palabra2="Python"
# palabra3="es"
# palabra4="genial"

# frase=" ".join([palabra1,palabra2,palabra3,palabra4])
# print(frase)



# resultado=texto.find("g")
# print(resultado)

# resultado=texto.find("E")
# print(resultado)

# resultado=texto.replace("Python","Otro lenguaje")
# print(resultado)

#####################################################################

# Frase1="La vida es bella"
# resultado=Frase1.upper()
# print(resultado)


# P1="Todo"
# P2="esta"
# P3="en"
# P4="constante"
# P5="cambio"
# Frase2=" ".join([P1,P2,P3,P4,P5])
# print(Frase2)



# Frase3= "Si la implementación es difícil de explicar, puede que sea una mala idea"
# Frase_modificada=Frase3.replace("difícil","fácil").replace("mala","buena")
# print(Frase_modificada)

#####################################################################
#No se puede
# nombre="Karolina"
# nombre[0]="C"
# print(nombre)
#Se Puede 
# n1="Caro" 
# n2="lina"
# print(n1+n2)
# print(n1*5)

# poema= """
# Esta es una linea del poema
# esta seria otra linea
# y esta otra linea
# """
# print(poema)

# print(len(poema))

# print("poema" in poema)
# print("sol" not in poema)

#####################################################################
#Listas
# mi_lista=["a","b","c"]
# mi_lista2=["e","f","g"]
# print(type(mi_lista))
# print(len(mi_lista))
# resultado=mi_lista[2]
# print(resultado)
# resultado=mi_lista[0:2]
# print(resultado)
# print(mi_lista+mi_lista2)
# mi_lista[0]="alfa"
# print(mi_lista)
# mi_lista.append("z")
# print(mi_lista)

# mi_lista.pop()
# print(mi_lista)

# mi_lista.pop(0)
# print(mi_lista)

# Lista=["z","a","h","u"]
# Lista.sort()
# print(Lista)

# Lista2=[100,50,40,200]
# Lista2.sort()
# print(Lista2)

# Lista2.reverse()
# print(Lista2)

#####################################################################
#Diccionarios

# diccionario={"c1":"valor1","c2":"valor2"}
# print(type(diccionario))
# resultado=diccionario["c2"]
# print(resultado)


# dic={"c1":55,"c2":[10,20,30],"c3":{"s1":100,"s2":200}}
# resultado=dic["c2"][1]
# print(resultado)
# resultado=dic["c3"]["s2"]
# print(resultado)


# dic2={"c1":["a","b","c"],"c2":["e","f","g"]}
# resultado=dic2["c2"][1].upper()
# print(resultado)

# dic3={1:"a",2:"b"}
# dic3[2]="c"
# print(dic3)

# dic3[3]="x"
# print(dic3)
# print(dic3.keys())
# print(dic3.values())
# print(dic3.items())
#####################################################################

# mi_dic={"nombre":"Karen","apellido":"Jurgens","edad":35,"ocupacion":"Periodista"}
# print(mi_dic)

# mi_dic["edad"]=36
# mi_dic["ocupacion"]="Editora"
# mi_dic["pais"]="Colombia"
# print(mi_dic)