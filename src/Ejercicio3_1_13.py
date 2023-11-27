import math 


def listas(lista: list, numeros: int) -> list:
    for i in range(0,numeros):
        numero = int(input(f"{i+1}) Escriba el número => "))
        lista.append(numero)
    return lista

def media(lista: list, numeros: int) -> float:
    cont = 0
    for num in lista:
        cont += num
    med = cont / numeros
    print(f"La media es: {med}")
    desviacion(lista, med, numeros)

def desviacion(lista:list,med:float, numeros: int) -> float:
    sumatoria = int(0)
    for num in lista:
        sumatoria += ((float(num) - med)**2)
    sumatoria = math.sqrt(sumatoria / numeros)
    print(f"La desviación típica es de: {sumatoria}")
    
def main():
    lista = list()
    numeros= int(input("¿Cuántos números vas a introducir? "))
    listas(lista, numeros)
    media(lista, numeros)
    



if __name__ == "__main__":
    main()
