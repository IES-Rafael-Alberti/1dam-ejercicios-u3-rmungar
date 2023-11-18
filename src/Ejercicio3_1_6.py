def asignaturas(materias:list, aprobadas: list):
    
    for materia in range(len(materias)):
        nota = float(input(f"Dime la nota que has sacado en {materias[materia]}: "))
        if nota >= 5:
            aprobadas.append(materias[materia])
    for materia in aprobadas:
        materias.remove(materia)
    return f"Tienes que recuperar: {materias}"


    

def main():
    materias = ["Matemáticas","Física","Química","Historia","Lengua"]
    aprobadas = []
    print(asignaturas(materias, aprobadas))
    
    
    
    
if __name__ == "__main__":
    main()
    