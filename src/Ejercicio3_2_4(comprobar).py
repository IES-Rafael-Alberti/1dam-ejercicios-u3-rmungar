def FeDiHo(Fecha, meses):
    Fecha.split(" / ")
    print(f"{Fecha[0]}, de, {meses[(Fecha[1])]}, del, {Fecha[2]}")





def main():
    fecha = (input("Ingrese una fecha con formato dd/mm/aaaa:"))
    meses = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}
    FeDiHo(fecha, meses)



if __name__ == "__main__":
    main()