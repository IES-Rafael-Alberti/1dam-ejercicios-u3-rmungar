def palindromo(lista: list):
    lista2 = lista.copy()
    lista2.reverse()
    if lista == lista2:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")
        
        
        
def main():
    lista=list(input("Ingrese una palabra: "))
    palindromo(lista)
    
    
    
if __name__ == "__main__":
    main()   