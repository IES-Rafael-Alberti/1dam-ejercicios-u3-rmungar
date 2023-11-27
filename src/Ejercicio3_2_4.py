def FeDiHo(Fecha:str, meses):
    Fechas = Fecha.split("/")
    print(f"{Fechas[0]} de {meses[int(Fechas[1])]} del {Fechas[2]}")



def main():
    Fecha = str(input("Ingrese una fecha con formato dd/mm/aaaa:"))
    meses = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}
    FeDiHo(Fecha, meses)



if __name__ == "__main__":
    main()