"""
Requisitos
Implementar un menú de aplicación con las siguientes opciones:
[1] Importar palabras clave
[2] Mostrar palabras clave
[0] Salir
Implementar una función carga_keywords() que lea un fichero llamado keywords.txt:
El fichero tendrá una(s) palabra(s) clave por línea.
No hay que separar las palabras clave con ningún carácter, solo enter.
El fichero se leerá línea a línea, guardando la palabra clave correspondiente como un nuevo elemento de una lista.
La función devolverá una lista de palabras clave.
Cuando se introduzca la opción de menú [1], se invocará a la función carga_keywords(). La lista resultante se asignará a una variable del programa llamada keywords.
Cuando se introduzca la opción de menú [2], se mostrará el listado de palabras clave de 20 en 20, es decir, una vez mostradas 20 palabras clave,
el usuario deberá pulsar la tecla enter para ver las siguientes.
Cuando se introduzca la opción de menú [0], el programa finalizará.
"""


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


def main():
    while True:
        print("Selecciona una opcion:")
        print("[1] Importar palabras clave")
        print("[2] Mostrar palabras clave")
        print("[0] Salir")
        option = input("Opcion: ")

        if option == "1":
            keywords = carga_keywords()
        elif option == "2":
            if "keywords" in locals():
                muestra_keywords(keywords)
            else:
                print("No se han importado palabras clave")
        elif option == "0":
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
