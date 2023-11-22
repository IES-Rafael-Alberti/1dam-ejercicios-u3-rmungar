def interseccion(numeros:set):
    pares = set()
    multiplos_de_tres = set()
    for e in numeros:
        if e%2 == 0:
            pares.add(e)
    for i in numeros:
        if i%3 == 0:
            multiplos_de_tres.add(i)
    pares_y_multiplos_de_tres = (pares & multiplos_de_tres)
    print(f"La intersección es => {pares_y_multiplos_de_tres}")
    
    
    
    
    
def main():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    interseccion(numeros)
    
    
    
if __name__ == '__main__':
    main()