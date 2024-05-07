"""
Escribe una función ordena_positivos(lista), que dada una lista de números enteros, devuelva
una nueva lista con los números positivos ordenados de menor a mayor, y mantenga los números
negativos en la misma posición que la lista original
"""


def ordena_positivos(numeros):
    ordenados = sorted([i for i in numeros if i > 0])
    for i in range(len(numeros)):
        if numeros[i] < 0:
            ordenados.insert(i, numeros[i])
    return ordenados


print(ordena_positivos([6, 3, -2, 5, -8, 2, -2]))
print(ordena_positivos([-5, -5, -5, -5, 7, -5]))
