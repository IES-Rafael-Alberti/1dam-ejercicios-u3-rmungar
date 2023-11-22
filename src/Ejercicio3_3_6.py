def unir(vocales) -> set:
    consonantes = {'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'}
    abecedario = vocales|consonantes
    print(abecedario)
    
    
    
    
def main():
    vocales = {'a','e','i','o','u'}
    unir(vocales)
    
    
    
if __name__ == '__main__':
    main()