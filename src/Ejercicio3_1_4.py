from BORRARCONSOLA import borrarconsola

def pedirnumero(Números:list):
    cont = 1
    while cont <= 6:
        numero= int(input(f"{cont} => "))
        if 0 < numero and numero < 50:
            while numero in Números:
                numero=int(input(f"""Número repetido, por favor ingrese un número no repetido. {cont} => """))
            Números.append(numero)
            
            cont+=1
        else:
            while 0>= numero or 50 <=numero:
                numero=int(input(f"""Número no válido, por favor ingrese un número valido. {cont} => """))
            if 0 < numero and numero < 50:
                while numero in Números:
                    numero=int(input(f"""Número repetido, por favor ingrese un número no repetido. {cont} => """))
                Números.append(numero)
                
                cont+=1
    lista_num(Números)

def lista_num(Números:list):
    Números.sort()
    reintegro = int(input("Ingrese el reintegro => "))
    while 0 > reintegro or 9 < reintegro:
        reintegro= int(input("Reintegro no válido, ingrese un reintegro válido 0-9 => "))
    Números.append(reintegro)
    print(f"Sus números de la Primitiva son: {Números}")    
    
def main():
    borrarconsola()
    print("Ingrese los números: ")
    Números=list("")
    
    pedirnumero(Números)
    
if __name__ == "__main__":
    main()    