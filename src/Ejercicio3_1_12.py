def productomatricial(m1: tuple, m2:tuple) -> tuple:
    return tuple(multiplicacion(m1[i],m2[i]) for i in range (len(m1)))


def multiplicacion(m1,m2):
    return tuple(m1[i]*m2[i] for i in range (len(m1)))
            


    
    
    
def main():
    m1= [(1,2) , (3,4) , (5,6)]
    m2= [(-1,0) , (0,1) , (1,1)]
    print(f"El producto de las matrices es: {productomatricial(m1, m2)}")



if __name__ == "__main__":
    main()