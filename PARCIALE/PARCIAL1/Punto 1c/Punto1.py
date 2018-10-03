def sumar (valor):
    ciclo = 0
    acum = 0
    dato = 1
    while ciclo != valor:
        ciclo = ciclo +1
        acum = acum + (dato*dato)
        print("\nEn el ciclo "+str(ciclo)+ " -> el valor actual de la suma de los digitos es: "+str(acum)+" sumando los datos hasta el "+ str(dato))
        dato = dato + 1
        
    return acum
def main():
    while (True):
        valor = int(input("Ingrese la cantidad de numeros que desea sumar al cuadrado,\n Si desea salir ingrese -1 = "))
        if valor == -1:
            break
        else:
            resul = sumar(valor)
            print("\nEl resultado para los "+ str(valor)+" primeros numeros es: ", resul)
            print("Su numero mínimo de operaciones es la misma cantidad de datos a sumar, es decir de  en O(n) = "+str(valor)+"\n")
        
        
main()
