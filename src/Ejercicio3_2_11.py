from BORRARCONSOLA import borrarconsola


def separador(lineas: str):
    datos = lineas.split("\n")
    datosC = datos[0].split(";")
    clasificador(datosC, datos)
        
        
def clasificador(datosC, datos):
    clientela = {}
    for i in datos[1:]:
        cliente = {}
        info = i.split(';') 
        for j in range(1,len(datosC)):

            if datosC[j] == 'descuento':
                info[j] = float(info[j])
            cliente[datosC[j]] = info[j]
        clientela[info[0]] = cliente
    print(clientela)
def main():
    borrarconsola()
    lineas = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
    
    separador(lineas)
    
    
    
    
    
if __name__ == "__main__":
    main()