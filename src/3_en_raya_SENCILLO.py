import os


FICHAS = (' ', 'X', 'O')


     
def borrarConsola():
    """Limpiar la consola"""
    
    os.system("cls")
    
    
def pulse_tecla_para_continuar():
    """Pausar hasta que se realize una acción"""
    
    os.system("pause")
     
     
def crearFila(numColumnas = 3) -> list:
    """Retorna una fila con los valores por defecto "0"= casilla vacía"""
    
    return list(0 for _ in range(numColumnas))
     
def crearTablero(numFilas = 3) -> tuple:
    """Crea un tablero 3x3, siendo numFilas el número de filas (3 por defecto) 
    y returna una tupla con la matriz numFilas x numColumnas"""
    
    return tuple(crearFila() for _ in range(numFilas))

def mostrarFila(fila:list):
    """Muestra una fila del tablero"""
    
    contenidoFila= "| "
    for celda in fila:
        contenidoFila += FICHAS[celda] + " | "
    print(contenidoFila)
    
def mostrarTablero(tablero: tuple):
    """Muestra el tablero en consola con las fichas"""
    
    borrarConsola()
    
    print("-" * 13)
    for fila in tablero:
        mostrarFila(fila)
        print("-" * 13)  

def cambiarTurno(turno: int) -> int: 
    """Modifica el turno e indica el jugador"""
    
    if turno % 2 == 0:
        return 1
    return 2

def pedirPoscición(filaCol: str, msj: str = ""):
    """Pide la posición de la ficha del usuario"""
    pos = None
    if msj != "": print(msj)
    while pos == None:
        try:
            pos = int(input(f"Elige la {filaCol} (1,2,3): ")) - 1
            if not 0<= pos <= 2:
                raise ValueError
        except ValueError:
            pos = None
            print(f"ERROR {filaCol} no válida")
    return pos       
            
def colocarFicha(tablero: tuple, jugador: int):
    """Solicita al jugador la posición de la ficha que va a colocar"""
    
    posFicha = {'fila': None, 'columna': None}
    posCorrecta = False
    
    while not posCorrecta:
        posFicha['fila'] = pedirPoscición("Fila",f"\nJugador {jugador}, coloque una ficha...")
        posFicha['columna'] = pedirPoscición("Columna")
        
        posCorrecta=comprobarCasilla(tablero, posFicha)
        if posCorrecta:
            tablero[posFicha['fila']][posFicha['columna']] == jugador
        else:
            posFicha['fila'] = posFicha['columna'] = None
            print("ERROR - Movimiento inválido")
            pulse_tecla_para_continuar()
            mostrarTablero(tablero)
    

def comprobarCasilla(tablero: tuple, posFicha: dict):
    """Comprueba el estado de las casillas del tablero"""
    return tablero[posFicha['fila']][posFicha['columna']] == 0

def comprobarGanador(tablero) -> tuple:
    None
def jugar(tablero: tuple):
    turno = 0
    ronda = 0
    hayGanador = False
    while not hayGanador:
        turno = cambiarTurno(turno)
        if turno == 1:
            ronda+=1
        print(f"\nRONDA {ronda}")
        print("-" * len(f"RONDA {ronda}" + "\n"))
        print(turno)
        
        colocarFicha(tablero, turno)
        mostrarTablero(tablero)
        
        if ronda >= 3:
            ganador, hayGanador = comprobarGanador(tablero)
        if hayGanador:
            print(f"\n ¡El jugador {ganador} ha ganado!\n")
        if ronda == 9:
            hayGanador = True
            print("\n¡EMPATE!\n")   
             
    
def main():
    tablero = crearTablero()   
    mostrarTablero(tablero)  
    jugar(tablero)
     
     
     
     
if __name__ == "__main__":
    main()