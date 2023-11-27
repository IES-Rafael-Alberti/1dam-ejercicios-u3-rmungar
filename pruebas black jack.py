import random
PALOS= [chr("3"), chr("6"), chr("5"), chr("4")]
CARTAS = ('As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
def crear_baraja() -> set:
    """ Crear la baraja de 52 cartas
    """
    p=random.randint(1,4)
    print(set((carta, p) for carta in (CARTAS, PALOS)))


def main():
    crear_baraja()


if __name__=="__main__":
    main()