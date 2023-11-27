def mayormenor(lista: list):
    lista.sort()
    print(f"El menor precio es: {lista[0]} y el mayor es: {lista[-1]}")
    
    
def main():
    lista = list([50, 75, 56, 22, 80, 65, 8])
    mayormenor(lista)
    
    
    
if __name__ == "__main__":
    main()