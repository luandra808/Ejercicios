#loop for
# lista=["a","b","c"]
# for letra in lista:
#     print(letra)
    
# for letra in lista:
#     numero_letra=lista.index(letra) + 1
#     print(f"Letra {numero_letra}: {letra}")


    
# lista2=["pablo","juan","andrea","lucia"]   
 
# for nombre in lista2:
#     if nombre.startswith("l"):
#         print(nombre)
#     else:
#         print("Este nombre no comienza con l")   
        
# for letra in "python":
#     print(letra)       
    
# for numero in [1,2,3,4]:
#     print(numero)
         
# for a,b in [[1,2],[3,4],[5,6]]: #mas de un elemento iterador
#     print(a)      
    
# dic={"clave1":"a","clave2":"b"}      

# for item in dic:
#     print(item)
    
# for item in dic.values():
#     print(item)
    
# for item in dic.items(): #lo muesra como tupla
#     print(item)
    
# for a,b in dic.items():
#     print(a,b)    
    
###########################################################################
#Ejercicio

# #1ro
# lista=["maria","jose","carlos","martina","isabel","tomas","daniela"]    
# for nombre in lista:
#     print("Hola " + nombre)

# #2do

# lista_numeros=[1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
# suma_numeros=0 #inicializar
# for numero in lista_numeros:
#     #suma_numeros= suma_numeros + numero
#     suma_numeros+=numero  # acumulador
# print(suma_numeros)

# #3ro

# suma_pares=0
# suma_impares=0

# for numero in lista_numeros:
#     if numero%2==0:
#         suma_pares+=numero
#     else:
#         suma_impares+=numero
# print(suma_pares)
# print(suma_impares)            


###########################################################################

#loop while
# monedas=5
# while monedas > 0:
#     print(f"tengo {monedas} monedas") #bucle infinito
#     monedas -=1 #salir del bucle reduciendo de una moneda
    
# respuesta="s"    
# while respuesta == "s":
#     respuesta=input("¿Quieres salir? (s/n)") 


###########################################################################

#range() = genera un objeto iterable

# for numero in range(1,5):
#     print(numero)    
    
# lista=list(range(1,20))
# print(lista)    


###########################################################################

#enumerate()

# lista=["a","b","c"]

# for item in enumerate(lista):
#     print(item)


# for indice,elemento in enumerate(lista):
#     print(indice,elemento)
    
# for indice,elemento in enumerate(range(50,55)):
#     print(indice,elemento)    
    
    
    
# mis_tuplas = list(enumerate(lista))    
# print(mis_tuplas)

###########################################################################

# print(list(enumerate("python")))

# lista_nombres=["Marcos","Laura","Monica","Javier","Celina","Marta","Dario","Emiliano","Melisa"]

# for i,nombre in enumerate(lista_nombres): #enumerate transforma en una tupla, por eso dos iteradores, i contiene el indice y nombre el elemnto
#     if nombre[0]=="M":
#         print (i) 

###########################################################################

#zip() = Combinacion de listas

# nombre=["Ana","Pedro","Lorena"]
# edades=[20,50,150,20,40]

# combinados=list(zip(nombre,edades)) #se generan tuplas de la combinacion
# print(combinados)

# for nombre,edad in combinados:
#     print(f"{nombre} tiene {edad}")

