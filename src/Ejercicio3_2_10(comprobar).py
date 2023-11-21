from BORRARCONSOLA import borrarconsola

def mostrar_menu():
    print("\nMenú:")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")


def agregar_cliente(base_datos:dict):
    nif = input("Ingrese el NIF del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    correo = input("Ingrese el correo del cliente: ")
    preferente = input("¿Es cliente preferente? (Sí/No): ").lower() == 'sí'
    if preferente in {'si','Si','Sí','sí','yes','Yes'}:
        preferente = 'Sí'
    else:
        preferente = 'No'
    #TODO: Crear un diccionario cliente con toda la información...
    cliente = {}
    cliente["Nombre"] = nombre
    cliente["Dirección"] = direccion
    cliente["Telefono"] = telefono
    cliente["Correo"] = correo
    cliente["Preferente"] = preferente

    #TODO: Añadir el diccionario cliente que previamente has creado al 
    # diccionario principal que hemos llamado base_datos...
    base_datos[nif] = cliente

    print(f"Cliente {nombre} añadido correctamente.")


def eliminar_cliente(base_datos:dict):
    nif = input("Ingrese el NIF del cliente que desea eliminar: ")
    #TODO: eliminar el cliente con nif que se ha introducido
    #Si existe mostrar por consola "Cliente con NIF XXXXXXXXX eliminado correctamente."
    #Sino mostrar "No se encontró un cliente con NIF XXXXXXXXX en la base de datos."
    if nif in base_datos:
        base_datos.popitem(nif)
    else:
        print(f"No se encontró un cliente con NIF {nif} en la base de datos.")


def mostrar_cliente(base_datos:dict):
    nif = input("Ingrese el NIF del cliente que desea mostrar: ")
    cliente = base_datos.get(nif)
    if cliente:
        print("\nDatos del cliente:")
        #TODO: Mostrar todos los datos del cliente
        #en cada línea de consola mostrar el par clave: valor de sus datos...
        for key, valor in base_datos[nif].items():
            print(f"{key} -> {valor}")
    else:
        print(f"No se encontró un cliente con NIF {nif} en la base de datos.")


def listar_clientes(base_datos:dict):
    print("\nListado de todos los clientes:")
    for nif, cliente in base_datos.items():
        print(f"NIF: {nif}, Nombre: {cliente['Nombre']}")


def listar_clientes_preferentes(base_datos:dict):
    print("\nListado de clientes preferentes:")
    for nif, cliente in base_datos.items():
        if cliente['Preferente']:
            print(f"NIF: {nif}, Nombre: {cliente['Nombre']}")


def main():
    borrarconsola()
    base_datos_clientes = {}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            agregar_cliente(base_datos_clientes)
        elif opcion == '2':
            eliminar_cliente(base_datos_clientes)
        elif opcion == '3':
            mostrar_cliente(base_datos_clientes)
        elif opcion == '4':
            listar_clientes(base_datos_clientes)
        elif opcion == '5':
            listar_clientes_preferentes(base_datos_clientes)
        elif opcion == '6':
            print("Programa terminado.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 6.")


if __name__ == "__main__":
    main()    
    
    
    
    
