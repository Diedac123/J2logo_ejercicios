"""
Implementar una función llamada ordena_ciudades(ciudades) que reciba como argumento un diccionario con ciudades y su población
y devuelva una lista con los nombres de las ciudades de más de 200.000 habitantes. La lista devuelta debe estar ordenada de mayor
a menor según el número de habitantes de cada ciudad.
"""


def ordena_ciudades(ciudades):
    return sorted(
        [k for k, v in ciudades.items() if v > 200000],
        key=lambda x: ciudades[x],
        reverse=True,
    )


ciudades = {"Valencia": 794000, "Salamanca": 144000, "Cádiz": 116000, "Madrid": 3200000}
print(ordena_ciudades(ciudades))
