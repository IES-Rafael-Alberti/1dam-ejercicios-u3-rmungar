def informacion(datos):
    print(f"{datos['nombre']} tiene {datos['edad']} años, vive en {datos['direccion']} y su número de teléfono es: {datos['telefono']}.")



def main():
    
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Inrgese la edad: "))
    direccion = input("Ingrese la dirección: ")
    telefono = int(input("Ingrese el teléfono: "))
    datos={'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
    informacion(datos)



if __name__ == "__main__":
    main()