import random


COLUMNAS = 8
FILAS = 8
VACIO = " "
MINA = "*"

tablero = [[VACIO for _ in range(COLUMNAS)] for _ in range(FILAS)]

def colocarMinas(tablero):
    for _ in range(10):
        columna = random.randint(0,7)
        fila = random.randint(0,7)
        tablero[fila][columna] = MINA
    return tablero, fila, columna
        
def calcular_numeros(tablero):
    """
    Esta función calcula el número de minas adyacentes a cada celda del tablero. Si la celda no contiene una mina, se coloca el número de minas adyacentes en la celda. Si la celda contiene una mina, se deja como está.
    :param tablero: tablero de juego
    """
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if tablero[fila][columna] != MINA:
                numero_minas = contar_minas_adyacentes(tablero, fila, columna)
                if numero_minas > 0:
                    tablero[fila][columna] = str(numero_minas)
                    
def contar_minas_adyacentes(tablero, fila, columna):
    """
    Esta función cuenta el número de minas adyacentes a la celda(i,j) seleccionada.
    :param tablero: tablero de juego
    :param fila: fila de la celda seleccionada
    :param columna: columna de la celda seleccionada
    :return: número de minas adyacentes a la celda(i,j) seleccionada
    """
    minas = 0
    for i in range(fila-1,fila+1):
        for j in range(columna-1,columna+1):
            if tablero[i][j] == MINA:
                minas+=1
    return minas
    


def main():
    colocarMinas(tablero)
    calcular_numeros(tablero)
    print(tablero)
    
    
    
if __name__ == "__main__":
    main()