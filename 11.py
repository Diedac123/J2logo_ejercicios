"""
En una votación, se dice que una opción tiene mayoría absoluta cuando el número de votos de la misma
es mayor que la mitad de los votos totales.
Implementar una función llamada mayoria_absoluta(votos) que, dada una lista de elementos (votos),
obtenga el elemento (voto) con mayoría absoluta, si existe.
"""


def mayoria_absoluta(votos):
    opciones = set(votos)
    for i in opciones:
        if votos.count(i) > len(votos) // 2:
            return i
    return False


votos = ["A", "A", "B", "C", "C", "C", "C"]
mayoria = mayoria_absoluta(votos)
if mayoria:
    print(f"{mayoria} tiene mayoria absoluta")
else:
    print("Nadie tiene mayoria absoluta")
