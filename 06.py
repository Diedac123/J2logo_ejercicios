"""
Escribe un programa de 3 lineas de codigo que reciba como entrada (por teclado) una secuencia de palabras separadas por espacios
en blanco e imprima las palabras ordenadas alfanuméricamente, en mayúsculas y después de haber eliminado todas las duplicadas.

Imagina que se proporciona la siguiente entrada al programa:

$> Lo mejor del lenguaje Python es que es un lenguaje del que no te aburres
La salida correspondiente al programa será:

ABURRES DEL ES LENGUAJE LO MEJOR NO PYTHON QUE TE UN
"""

frase = input("Escribe la frase: ")
frase = " ".join(sorted(set((frase).upper().split(" "))))
print(frase)
