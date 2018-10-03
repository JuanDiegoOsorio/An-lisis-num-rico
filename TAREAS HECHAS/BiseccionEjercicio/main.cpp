#include <iostream>

using namespace std;
#include <math.h>
double nseccion(double, double, int,int);


int main()
{

    double sup, inf;
    int particiones;
    cout<<"Ingrese el limite superior y el inferior: "<<endl;
    cin>>sup>>inf;
    cout<<"Ingrese el numero de particicones: "<<endl;
    cin>>particiones;
    cout<<"\nEl valor es: "<< nseccion(sup,inf,particiones,0);

    return 0;
}

double nseccion(double plot1, double plot2, int particion, int iteraciones){
    
    //como comprobar que f(a) y f(b) < 0 y para cual funcion
    // Funcion = x^3
    
    iteraciones++;
    
    cout<<"\n Iteracion #"<<iteraciones<<": El error es= "<<plot2-plot1;
    
    double value1 = (plot2+plot1)/pow(2,particion);
    
    if (pow(plot1,3)*pow(value1,3)==0){
        return value1;
    }
    
    if (pow(plot1,3)*pow(value1,3)<0){
        plot2 = value1;
        return nseccion(plot1,plot2, particion, iteraciones);
    }

    if (pow(plot1,3)*pow(value1,3)>0){
        plot1 = value1;
        return nseccion(plot1,plot2, particion, iteraciones);
    }
