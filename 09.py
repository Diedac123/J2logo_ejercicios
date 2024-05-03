"""
Implementar una función mapa_caracteres(palabra) que devuelva un mapa de caracteres único de una palabra.

El mapa de caracteres es una lista numérica en la que el número 0 se corresponde con el primer carácter de la palabra,
el 1 con el siguiente carácter diferente y así, sucesivamente
"""


def mapa_caracteres(palabra):
    letras = {}
    mapa = []
    numero = 0
    for i in palabra:
        if i not in letras:
            letras[i] = numero
            numero += 1
        mapa.append(letras[i])
    return mapa


palabra = input("ingrese una palabra: ")
print(mapa_caracteres(palabra))
