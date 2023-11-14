def productoescalar(v1: tuple, v2:tuple) -> tuple:
    return tuple(v1[i]*v2[i] for i in range(len(v1)))
    
    
    
    
def main():
    v1= [1,2,3]
    v2= [-1,0,2]
    print(productoescalar(v1, v2))



if __name__ == "__main__":
    main()