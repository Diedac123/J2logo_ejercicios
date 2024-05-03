"""
Escribe un programa que, dada una cadena de texto que se introduce por consola, cuente y muestre el número de apariciones de cada 
carácter en la cadena. Como te decía, debes usar el tipo dict para almacenar los resultados.
Imagina que se introduce la siguiente cadena:
$> 'abcdasdfacdjop'
La salida del programa debería ser algo similar a esto (el orden puede no ser el mismo):

a: 3
b: 1
c: 2
d: 3
s: 1
f: 1
j: 1
o: 1
p: 1
"""

letras = {}
palabra = input("Ingrese la palabra: ")
# for i in palabra:
#     if i in letras:
#         letras[i] += 1
#     else:
#         letras[i] = 1

# for i in letras:
#     print(f"{i}: {letras[i]}")

# otro metodo

for c in palabra:
    letras[c] = letras.get(c, 0) + 1
print("\n".join([f"{k}: {v}" for k, v in letras.items()]))
