def asignaturas(materias:list):
    
    for materia in range(len(materias)):
        nota = float(input(f"Dime la nota que has sacado en {materias[materia][0]}: "))
        materias[materia][1] = nota
        print(f"En {materias[materia][0]} has sacado un {materias[materia][1]}")
    

def main():
    materias = (["Matemáticas",0],["Física",0],["Química",0],["Historia",0],["Lengua",0])
    asignaturas(materias)
    
    
    
if __name__ == "__main__":
    main()
    