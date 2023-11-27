
def saltos(abecedario:list) -> list:
    for letra in abecedario[::3]:
        abecedario.remove(letra)
    print(abecedario)   


def main():
    abecedario = list("abcdefghijklmnñopqrstuvwxyz")
    saltos(abecedario)

if __name__ == "__main__":
    main()