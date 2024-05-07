"""
Implementa una función acumulado(lista), a la que se le pase como argumento una lista de números
enteros y devuelva una lista de la suma acumulada
"""

# def acumulado(lista):
#     acumulado = []
#     for i in range(len(lista)):
#         if i == 0:
#             acumulado.append(lista[i])
#         else:
#             acumulado.append(lista[i] + acumulado[i - 1])
#     return acumulado


# mas pitonica
def acumulado(lst):
    return [sum(lst[: i + 1]) for i in range(len(lst))]


print(acumulado([1, 5, 7]))
print(acumulado([1, 0, 1, 0, 1]))
print(acumulado([]))
