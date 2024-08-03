# #Tuplas
# mi_tupla=(1,2,3,4)
# print(type(mi_tupla))

# t=(1,"hola",3.2)
# # mi_tupla[0]=7
# # print(mi_tupla)
# mi_tupla2=(1,2,(2,4),6)
# print(mi_tupla2[2][1])
# mi_tupla=list(mi_tupla)
# print(mi_tupla)
# print(type(mi_tupla))


# t=(1,2,3,7,1)
# x,y,z,u,v=t
# print(t.count(1))

####################################################
#ejercicio
# mi_tupla=(1,2,3,2,3,1,3,2,3,3,3,1,3,2,2,1,3,2)
# print(mi_tupla.count(2))
# mi_tupla=(1,2,3,2,3,1,3,2)
# mi_lista=list(mi_tupla)
# print(mi_lista)
# mi_tupla=(1,2,3,4)
# w,x,y,z=mi_tupla
# print(w,x,y,z)

####################################################

#sets/conjuntos

# mi_set=set([1,2,3,4,5,6])
# mi_set=set({1,2,3})
# mi_set=set((1,2,3))
# mi_set={1,2,3}
# print(mi_set)
# print(len(mi_set))
# conjunto={1,2,3,4,5,6,7,8,9,1,1} # no muestra elementos duplicados
# print(conjunto)
# print(2 in conjunto)
# s1={1,2,3}
# s2={3,4,5}
# s3=s1.union(s2)
# print(s3)
# s1.add(4)
# print(s1)

# s1.clear()
# print(s1)

####################################################
#booleanos

# mi_bool=True
# mi_boll=False
# numero=5>6
# print(numero)
# lista=[1,2,3,4]
# control=2 in lista
# print(control)

#ejercicios booleanos

# Comparacion=6>8
# prueba=False
# print(comparacion)

# operacion_1=17834/34
# operacion_2=87*56
# comparacion=operacion_1>operacion_2
# print(comparacion)


# comparacion= 25**0.5==5
# print(comparacion)

####################################################

#operadores lógicos


# a=10
# b=5
# c=15
# print(a>b and a<c)
# print(a>b or a>c)


# texto="esta frase es breve"
# mi_bool=("frase" in texto) or ("python"in texto)
# print(mi_bool)
# mi_bool= not"a"=="a"
# print(mi_bool)

####################################################

#Condicionales

# if 10>9:
#     print("Es correcto")
    
# if True:
#     print("Es correcto")
    
    
    
# if 2==5:
#     print("Es correcto")
# else:
#     print("No es correcto")
    
    
# mascota="perro"
# if mascota=="perro":
#     print("tu mascota es un perro")
# elif mascota=="gayo":
#     print("tu mascota es un gato")
# elif mascota=="loro":
#     print("tu mascota es un loro")
# else:
#     print("No tienes mascotas")
    
    
    
# Edad= 15
# Calificacion=5

# if Edad < 18:
#     print("Eres menor de edad")
#     if Calificacion >=3:
#         print("Aprobaste el curso")
#     else:
#         print("No aprobaste el curso")    
# else:
#     print("Eres adulto")


#Ejercicio

num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese otro numero: "))

if num1>num2:
    print(f"{num1} es mayor que {num2}")
elif num2>num1:
    print(f"{num2} es mayor que {num1}")
elif num1==num2:
    print(f"{num1} y {num2} son iguales")