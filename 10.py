"""
Implementar una función cuadrado(n) que tome como argumento un número entero n y genere
un cuadrado de n x n formado, precisamente, por el número n
"""


def cuadrado(n):
    return [[n] * n] * n


if __name__ == "__main__":
    n = int(input("Ingrese el largo del cuadrado: "))
    for i in cuadrado(n):
        print(i)
