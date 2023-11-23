from BORRARCONSOLA import borrarconsola

def datos(factura:set):
    domicilio = set()
    for dato in factura:
        domicilio.add(dato[3])
    print(f"Se han de enviar a los siguientes domicilios: {domicilio}")
        




def main():
    borrarconsola()
    factura = [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]
    datos(factura)



if __name__=="__main__":
    main()