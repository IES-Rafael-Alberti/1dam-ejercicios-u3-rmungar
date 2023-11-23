def lista_de_la_compra(lista):
    ingreso = True
    cont = 1
    total = 0
    while ingreso == True:
        clave = input(f"Artículo {cont}: ")
        valor = int(input(f"Ingrese el precio de {clave}: €"))
        lista[clave] = int(valor)
        total += valor
        terminar= input("¿Terminar? (s/n): ")
        cont+=1
        if terminar == "s":
            ingreso=False
            print(total,'€')
        


def main():
    lista={'Artículo': 'Precio'}
    lista_de_la_compra(lista)



if __name__ == "__main__":
    main()