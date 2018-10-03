import math
def funcion(valor):
    return  math.sin(valor)

        
def main():

    print("El primer valor del intervalo = -1")
    print("El segundo valor del intervalo es -2 ")
    exacto = -1.6314435
    print("El valor exacto debe ser =  ",exacto)
    ext1 = -1
    ext2 = -2
    Valn = ext2
    while (exacto != Valn):
        Valn = ext1 - funcion(ext1) *( (ext1 - ext2) / funcion( ext1 ) - funcion(ext2) )
        Valn = round(Valn,7)
        print("Valn = ",Valn)
        print("Error = "+str(abs(exacto-Valn)))
        
main()
