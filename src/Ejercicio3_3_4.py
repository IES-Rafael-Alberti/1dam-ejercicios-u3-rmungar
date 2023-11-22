def comparador(frutas1,frutas2):
    frutas_comunes = set()
    frutas_solo_en_frutas1 = set()
    frutas_solo_en_frutas2 = set()
    for fruta in frutas1:
        if fruta in frutas2:
            frutas_comunes.add(fruta)
        elif fruta not in frutas2:
            frutas_solo_en_frutas1.add(fruta)
    print(f"Frutas comunes: {frutas_comunes}")
    print(f"Frutas exclusivas de Frutas1: {frutas_solo_en_frutas1}")
    for fruta in frutas2:
        if fruta not in frutas1:
            frutas_solo_en_frutas2.add(fruta)
    print(f"Frutas exclusivas de Frutas2: {frutas_solo_en_frutas2}")


def main():
    frutas1 = ["manzana","pera","naranja","platano","uva"]
    frutas2 = ["manzana","pera","durazno","sandía","uva"]
    comparador(frutas1,frutas2)
    
    
    
    
if __name__ == "__main__":
    main()