#include <iostream>

using namespace std;
#include <math.h>
double nseccion(double, double, int,int);


int main()
{

    double sup, inf;
    int particiones;
    cout<<"Ingrese el límite superior y el inferior: ";
    cin>>sup>>inf;
    cout<<"\nIngrese el número de particicones";
    cin>>particiones;
    
    cout<<"\nEl valor es: "<< nseccion(sup,inf,particiones,0);

    return 0;
}

double nseccion(double plot1, double plot2, int particion, int iteraciones){
    
    //como comprobar que f(a) y f(b) es < que 0
    
    iteraciones++;
    double value1 = (plot2-plot1)/pow(2,particion);
    
    if (plot1*value1==0){
        return value1;
    }
    
    if (plot1*value1<0){
        plot2 = value1;
        return nseccion(plot1,plot2, particion, iteraciones);
    }

    if (plot1*value1>0){
        plot1 = value1;
        return nseccion(plot1,plot2, particion, iteraciones);
    }
