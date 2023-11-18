def ampliacion(dict):
    ingreso = True
    while ingreso == True:
        clave = input("Ingrese la clave para el valor del diccionario: ")
        valor = input("Ingrese un valor: ")
        dict[clave] = valor
        print(dict)
        cont= input("¿Deseas seguir ampliando el diccionario? (s/n): ")
        if cont == "n":
            ingreso=False



def main():
    dict={}
    ampliacion(dict)



if __name__ == "__main__":
    main()