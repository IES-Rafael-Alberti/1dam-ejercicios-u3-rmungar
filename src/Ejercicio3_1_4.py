def pedirnumero(Números:list, Números2:list):
    cont = 1
    while cont <= 6:
        numero= int(input(f"{cont} => "))
        if 0 < numero and numero < 50:
            while numero in Números2:
                numero=int(input(f"""Número repetido, por favor ingrese un número no repetido. {cont} => """))
            Números.append(numero)
            Números2.append(numero)
            cont+=1
        else:
            while 0> numero or 50 <=numero:
                numero=int(input(f"""Número no válido, por favor ingrese un número valido. {cont} => """))
            if 0 < numero and numero < 50:
                while numero in Números2:
                    numero=int(input(f"""Número repetido, por favor ingrese un número no repetido. {cont} => """))
                Números.append(numero)
                Números2.append(numero)
                cont+=1
    lista_num(Números)

def lista_num(Números):
    Números.sort()
    reintegro = int(input("Ingrese el reintegro => "))
    while 0 > reintegro or 9 < reintegro:
        reintegro= int(input("Reintegro no válido, ingrese un reintegro válido 0-9 => "))
    Números.append(reintegro)
    print(f"Sus números de la Primitiva son: {Números}")    
    
def main():
    print("Ingrese los números: ")
    Números=list("")
    Números2=list("")
    pedirnumero(Números,Números2)
    
if __name__ == "__main__":
    main()    