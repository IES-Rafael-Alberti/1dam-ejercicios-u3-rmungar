import os
def borrarconsola():
    os.system("cls")


def recogepalabras(diccionario: dict) -> dict:
    ingreso = True
    while ingreso:
            palabras = input("Ingrese una palabra y su traducción separadas por : => ")
            if palabras != "":
                Palabra = palabras.split(":")
                diccionario[Palabra[0]] = Palabra[1]
            else:
                ingreso = False
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
    advertencia = ("Para dejar de introducir palabras, ingrese un espacio en blanco.")
    print(advertencia)
    recogepalabras(diccionario)
    frase = recogefrase()
    traductor(diccionario,frase)



if __name__=="__main__":
    main()