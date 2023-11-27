import os
def borrarconsola():
    os.system("cls")


def recogepalabras(diccionario: dict) -> dict:
    palabras = input("Ingrese palabra:traducción separadas por comas => ")
    ingresos = palabras.split(", ")
    for item in ingresos: 
        Palabra = item.split(":")
        diccionario[Palabra[0]] = Palabra[1]
    return diccionario
         
             
def recogefrase() -> str:
    frase = str(input("Ahora ingrese una frase para traducir: "))
    return frase


def traductor(diccionario: dict, frase: str) -> str:
    Frase = frase.split(" ")
    resultado = ""
    for palabra in Frase:
        if palabra not in diccionario:
            resultado += palabra + " "
        else: 
            resultado += (diccionario[palabra]) + " "
    print(resultado)


def main():
    borrarconsola()
    diccionario = {}
    recogepalabras(diccionario)
    frase = recogefrase()
    traductor(diccionario,frase)



if __name__=="__main__":
    main()