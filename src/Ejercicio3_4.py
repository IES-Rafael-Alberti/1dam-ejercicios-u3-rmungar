

    
    
def lista_num(reintegro,Números):
    Números.sort()
    Números.append(reintegro)
    return Números    
    
def main():
    print("Ingrese los números: ")
    Números=list("")
    cont = 1
    while cont <= 6:
        numero= int(input(f"{cont} => "))
        Números.append(numero)
        cont += 1
    if cont == 7:
        reintegro = int(input("Reintegro => ")) 
    
       
    print(lista_num(reintegro, Números))
    
if __name__ == "__main__":
    main()    