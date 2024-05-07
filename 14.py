"""
Implementa una función siguiente_mayor(lista), a la que se le pase como argumento una lista de números
enteros y reemplace cada número por el siguiente más grande de la lista.
"""

# def siguiente_mayor(lista):
#     siguiente_mayor = []
#     ordenada = sorted(lista)
#     for numero in lista:
#         if numero == ordenada[-1]:
#             siguiente_mayor.append(-1)
#         else:
#             i = ordenada.index(numero) + 1
#             siguiente_mayor.append(ordenada[i])
#     return siguiente_mayor

# mas pythonica


def siguiente_mayor(lst):
    asc = sorted(lst) + [-1]
    return [asc[asc.index(i) + 1] for i in lst]


print(siguiente_mayor([5, 7, 3, 2, 8]))
print(siguiente_mayor([1, 0, -1, 8, -72]))
