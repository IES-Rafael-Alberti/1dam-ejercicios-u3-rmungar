
def comprobardict(divisa: str, divisas: dict):
    divisa.capitalize()
    if divisa not in divisas:
        print(f"La divisa introducida ({divisa}), no está en el diccionario")
    else:
        print(divisas[divisa])


def main():
    divisas = {'Euro': "€", 'Dolar': "$", 'Yen': "¥"}
    divisa = input("Ingrese una el nombre de una divisa: ")
    comprobardict(divisa, divisas)





if __name__ == "__main__":
    main()