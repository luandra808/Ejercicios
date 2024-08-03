# texto=input("Ingrese su texto: ").lower()
# letras=input("Ingrese 3 letras: ").lower()
# mi_lista=[letras[0],letras[1],letras[2]]
# print(f"La letra {mi_lista[0]} se repite {texto.count(mi_lista[0])} veces \nLa letra {mi_lista[1]} se repite {texto.count(mi_lista[1])} veces \nLa letra {mi_lista[2]} se repite {texto.count(mi_lista[2])} veces ")


texto=input("Ingrese su texto: ").lower()
letras=input("Ingrese 3 letras: ").lower()
texto_lista=texto.split()
# 1er punto
print(f"La letra {letras[0]} se repite {texto.count(letras[0])} veces \nLa letra {letras[1]} se repite {texto.count(letras[1])} veces \nLa letra {letras[2]} se repite {texto.count(letras[2])} veces ")
# 2do punto
print(f"La cantidad de palabras en tú texto es: {len(texto_lista)}")
# 3er punto
resultado1= texto_lista[0][0]
resultado2= texto_lista[-1][-1]
print(f"La primera letra de tú texto es: {resultado1} y la última letra es: {resultado2}")
# 4to punto
texto_lista.reverse()
union=" ".join(texto_lista)
print(f"Asi quedaría su texto si se invertiera el orden de las palabras: {union}")
#5to punto
Busqueda= "python" in texto
diccionario={True:"si",False:"no"}
print(f"La palabra python {diccionario[Busqueda]} esta en el texto")
