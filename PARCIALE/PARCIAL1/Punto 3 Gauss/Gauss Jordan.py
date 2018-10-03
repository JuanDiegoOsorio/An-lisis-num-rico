


def imprimir(matriz, filas):
    for i in range(filas):
            print(matriz[i])

def divFilaAbajo (matriz, indice):
    for i in range (indice, len(matriz)):
        valor = matriz[i][indice]
        for j in range(indice,len(matriz[i])):
            matriz[i][j] = matriz[i][j]/valor

            
def multiYsum (matriz, indice):
    for i in range(indice+1, len(matriz)):
        for j in range(indice, len(matriz[i])):
            matriz[i][j]+= matriz[indice][j]*(-1)


def divAlRevez(matriz, indice):
    for i in range(len(matriz)-1, -1, -1):
        print ("VALOR DEl I = "+str(i)+" "+"INDICE = "+str(indice))


"""
def validarMatriz (matriz):
    flagFila = False
    flagResultado = False
    
    for i in range(len(matriz)):
        flagFila = False
        flagResultado = matriz [i][len(matriz[i])-1] != 0
        
        for j in range(len(matriz[i])-1):
            if (matriz[i][j] != 0):
                flagFila = True
                break
            print("VALOR DE I Y J = "+str(i)+" "+str(j))
            print("FLAG FILA y FLAG RESULTADO= "+str(flagFila)+" "+str(flagResultado))

        if not(flagFila and flagResultado):
            return False
    return True

"""


def main():

    print ("METODO DE GAUSS-JORDAN\n")
    filas = int(input("Ingrese el numero de filas de la matriz: "))
    columnas = int (input("Ingrese el numero de columnas de la matriz: "))
    matrisinia = []
    for i in range (filas):
        matrisinia.append([])
        for j in range(columnas):
            matrisinia[i].append(float(input("Ingrese el dato en la posición "+str(i)+","+str(j)+": ")))
    imprimir(matrisinia, filas)
    
    


    for i in range(filas):
        for j in range (filas):
            if matrisinia[i][0]< matrisinia[j][0]:
                aux = matrisinia[i]
                matrisinia[i] = matrisinia [j]
                matrisinia[j] = aux
    print ("Matriz ordenada: ")
    imprimir(matrisinia, filas)
    
    for i in range (filas):
        divFilaAbajo(matrisinia,i)
        print("MATRIZ DIVIDIDA HACIA ABAJO, DEBE HABER FILA DE UNOS: ")
        imprimir(matrisinia, filas)
        multiYsum(matrisinia, i)
        print("MULTIPLICACIÓN Y SUMA DE FILAS: ")
        imprimir(matrisinia, filas)
        print("\n\n\n")
        
    for i in range(filas, -1, -1):
        divAlRevez(matrisinia, i)

"""
    
    for i in range(filas):
        valor = matrisinia[i][i ]
        for j in range (columnas):
            matrisinia[i][j]= matrisinia[i][j]/ valor
    imprimir(matrisinia, filas)

    for i in range (1, filas):
        for j in range (columnas):
            matrisinia[i][j] += -1*matrisinia[0][j]

"""
            
    
main()
    
