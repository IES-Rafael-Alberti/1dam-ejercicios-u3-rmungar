def asignaturas(materias:list):
    
    for materia in range(len(materias)):
        print(f"Yo estudio {materias[materia]}")
    
    
    
def main():
    materias = ["Matemáticas","Física","Química","Historia","Lengua"]
    asignaturas(materias)
    
    
    
if __name__ == "__main__":
    main()
    