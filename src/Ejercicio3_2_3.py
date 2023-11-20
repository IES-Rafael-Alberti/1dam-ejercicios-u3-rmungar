def comprobarFruta(fruteria, fruta: str):
    fruta.capitalize()
    if fruta in fruteria:
        total(fruta, fruteria)
    else:
        print(f"La fruta seleccionada, ({fruta}), no esta en el diccionario")


def total(fruta, fruteria):
    cantidad = int(input("¿Cuántos kilos quieres?: "))
    tot = cantidad * fruteria[fruta]
    print(tot)



def main():
    fruteria = {'Platano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}
    fruta = (input("Eliga una fruta: "))
    comprobarFruta(fruteria, fruta)

if __name__ == "__main__":
    main()