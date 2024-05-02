"""
Implementar una función comprueba_keywords(kw, dominio).
Esta función define dos parámetros: kw es un string con la keyword o keywords a buscar; dominio es el dominio para el que se quiere 
comprobar la posición en que rankea la palabra clave kw.
La función debe devolver la posición para la que rankean las palabras clave kw para el dominio dominio.
Si no se ha encontrado en las primeras 100 posiciones, la función devolverá por defecto el valor 100.
Añadir una variable al programa con el dominio a tener en cuenta (puedes elegir el dominio que prefieras para trabajar).
Añadir una nueva opción de menú al programa: [3] - Comprobar palabras clave.
Cuando el usuario seleccione en el menú la opción 3, el programa solicitará al usuario qué palabras clave quiere comprobar y
seguidamente invocará a la función comprueba_keywords().
Además, se mostrará en qué posición rankean las palabras clave o si no rankean (la función devuelve el valor 100).
"""

import requests
from bs4 import BeautifulSoup


def carga_keywords():
    keywords = []
    with open(
        r"C:\Users\ddacunto.DGOGPP\Proyectos\J2logo_ejercicios\seguimiento_google\keywords.txt",
        "r",
        encoding="utf-8",
    ) as file:
        for line in file:
            keywords.append(line.strip())
    return keywords


def muestra_keywords(keywords):
    for i in range(0, len(keywords), 20):
        print("\n".join(keywords[i : i + 20]))
        input("Pulsa enter para continuar...")


def aparece_el_dominio(link, dominio):
    encontrado = False
    fin = link.find("&")
    pagina = link[:fin]
    if dominio in pagina:
        encontrado = True
    return encontrado


def comprueba_keywords(kw, dominio):
    continuar = True
    start = 0
    posicion = 1
    encontrado = False
    while continuar and not encontrado:
        parametros = {"q": kw, "start": start}
        resp = requests.get(f"https://www.google.com/search", params=parametros)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, "lxml")
            div_principal = soup.find("div", {"id": "main"})
            resultados = div_principal.find_all("div", class_="ZINbbc xpd O9g5cc uUPGi")
            for res in resultados:
                if res.div and res.div.a:
                    if aparece_el_dominio(res.div.a["href"], dominio):
                        encontrado = True
                        break
                    else:
                        posicion += 1
            if not encontrado:
                footer = div_principal.find("footer")
                siguiente = footer.find("a", {"aria-label": "Página siguiente"})
                if siguiente:
                    start += 10
                    if start == 100:
                        continuar = False
                else:
                    continuar = False
        else:
            continuar = False
    if not encontrado:
        posicion = 100
    return posicion


def main():
    dominio = "https://developer.algorand.org/"
    while True:
        print("Selecciona una opcion:")
        print("[1] Importar palabras clave")
        print("[2] Mostrar palabras clave")
        print("[3] Comprobar palabras clave")
        print("[0] Salir")
        option = input("Opcion: ")

        if option == "1":
            keywords = carga_keywords()
        elif option == "2":
            if "keywords" in locals():
                muestra_keywords(keywords)
            else:
                print("No se han importado palabras clave")
        elif option == "3":
            kw = input("Introduce la(s) palabra(s) clave a buscar: ")
            posicion = comprueba_keywords(kw, dominio)
            if posicion == 100:
                print(
                    "No se ha encontrado la palabra clave en las primeras 100 posiciones"
                )
            else:
                print(f"La palabra clave se encuentra en la posición {posicion}")
        elif option == "0":
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
