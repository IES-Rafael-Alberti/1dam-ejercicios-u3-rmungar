from BORRARCONSOLA import borrarconsola


def separador(lineas: str):
    linea = lineas.split("\n")
    nom_campos = linea[0]
    datos = lineas.split(";")
    clasificador(nom_campos, datos)
        
        
def clasificador(nom_campos, datos):
    Diccionario = {}
    if len(nom_campos) == len(datos):
        for i in range(len(nom_campos)):
            Diccionario[nom_campos[i]]=datos[i]
    print(Diccionario)

def main():
    borrarconsola()
    lineas = """nif;nombre;email;teléfono;descuento\n
    01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n
    71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n
    63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n
    98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"""
    
    separador(lineas)
    
    
    
    
    
if __name__ == "__main__":
    main()