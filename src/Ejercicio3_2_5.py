def creditos(curso:dict):
    credsTotales = 0
    for asignatura, creds in curso.items():
        print(f"{asignatura} tiene {creds} créditos")
        credsTotales += creds
    print(f"Hacen un total de {credsTotales} créditos")




def main():
    curso = {'Matemáticas':6, 'Física': 4, 'Química':5}
    creditos(curso)



if __name__ == "__main__":
    main()