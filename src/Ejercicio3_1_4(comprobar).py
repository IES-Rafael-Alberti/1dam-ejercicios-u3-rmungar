def pedirnumero(Números:list, Números2):
    cont = 1
    numero= int(input(f"{cont} => "))
    while cont <= 6:
        if 0<numero<50:
            if numero in Números2:
                print("Introduzca un número válido => ")
                numero = int(input(f"{cont} => "))
            else:
                Números.append(numero)
        else:
            print("Ingrese un número válido")
            numero = int(input(f"{cont} => "))
        cont+=1
    if cont == 7:
        reintegro = int(input("Reintegro => "))
        if 0 > reintegro or reintegro > 9:
            while 0 > reintegro or 9 < reintegro:
                print("Reintegro no válido")
                reintegro = int(input("Ingrese un reintegro válido"))  
    return Números, reintegro
    
    
def lista_num(Números, reintegro):
    Números.sort()
    Números.append(reintegro)
    print (Números)    
    
def main():
    print("Ingrese los números: ")
    Números=list("")
    Números2=list("")
    pedirnumero(Números,Números2)
    lista_num(Números)
    
if __name__ == "__main__":
    main()    