from BORRARCONSOLA import borrarconsola

def datos(factura:set):
    ingresos = True
    while ingresos == True:
        ingreso = input("¿Desea añadir una factura? ")
        if ingreso in {'si','sí','Si','Sí','yes','Yes'}:
            factura.add(input("Ingrese la información de la venta => "))
        elif ingreso in {'no','No'}:
            ingresos = False

def facturacion(factura:set):





def main():
    factura = set(cliente, dia_mes, monto, domicilio)





if __name__=="__main__":
    main()