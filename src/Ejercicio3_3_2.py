from BORRARCONSOLA import borrarconsola


def pedirNombresPrimaria(alumnosPrimaria:set):
    ingreso = True
    while ingreso == True:
        nombre = str(input("Introduzca los nombres de los alumnos de primaria: "))
        alumnosPrimaria.add(nombre)
        if nombre == "x" or nombre == "X":
            ingreso = False


def pedirNombresSecundaria(alumnosSecundaria):
    ingreso = True
    while ingreso == True:
        nombre = str(input("Introduzca los nombres de los alumnos de secundaria: "))
        alumnosSecundaria.add(nombre)
        if nombre == "x" or nombre == "X":
            ingreso = False
        
def mostrarTodo(alumnosPrimaria:set, alumnosSecundaria:set):
    alumnosPrimaria.remove("x")
    alumnosSecundaria.remove("x")
    todosAlumnos = (alumnosPrimaria | alumnosSecundaria)
    print(f"Todos los alumnos: {todosAlumnos}")
    
    
def repetidos(alumnosPrimaria, alumnosSecundaria):
    repeticiones = (alumnosPrimaria & alumnosSecundaria) 
    print(f"Los nombres repetidos son: {repeticiones}")
    

def noRepetidos(alumnosSecundaria, alumnosPrimaria):
    a = (alumnosSecundaria-alumnosPrimaria)
    b = (alumnosPrimaria-alumnosSecundaria)
    unicos = (a|b)
    print(f"Los nombres no repetidos son: {unicos}")
    
    
def comparativa(alumnosPrimaria, alumnosSecundaria):
    if alumnosPrimaria == alumnosSecundaria:
        print("Todos los nombres de primaria estan en secundaria")
    else:
        print("No todos los nombres de primaria estan en secundaria")
    
def main():
    borrarconsola()
    alumnosPrimaria = set()
    alumnosSecundaria = set()
    pedirNombresPrimaria(alumnosPrimaria)
    pedirNombresSecundaria(alumnosSecundaria)
    mostrarTodo(alumnosPrimaria, alumnosSecundaria)
    repetidos(alumnosPrimaria, alumnosSecundaria)
    noRepetidos(alumnosPrimaria, alumnosSecundaria)
    comparativa(alumnosPrimaria,alumnosSecundaria)
    
    
    
if __name__ == "__main__":
    main()