def pedir_palabra() -> tuple:
    palabra = tuple(input("Dame una palabra: ").lower())
    return palabra

def cuentavocales(palabra: tuple) -> tuple:
    vocales = (["a",0],["e",0],["i",0],["o",0],["u",0])
    for vocal in vocales:
        vocal[1] = palabra.count(vocal[0])
    return vocales
    
def recuento(vocales):    
    for vocal in vocales:
        print(f"{vocal[0]} => {vocal[1]}")
    
def main():
    palabra = pedir_palabra()
    vocales = cuentavocales(palabra)
    recuento(vocales)
    
    
    
if __name__ =="__main__":
    main()
    