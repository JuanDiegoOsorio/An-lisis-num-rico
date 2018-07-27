#include <iostream>

using namespace std;

double triseccion(double, double);


int main()
{

    return 0;
}

double triseccion(double plot1, double plot2){

    double value1 = (plot1+plot2)/3;
    double value2 = (2*(plot1+plot2))/3;

    if (plot1*value1==0){
        return value1;
    }
    if (value1*value2==0){
        return value2;
    }
    if (value2*plot2==0){
        return plot2;
    }

    if (plot1*value1<0){
        plot2 = value1;
        return triseccion(plot1,plot2);
    }
    if (value1*value2<0){
        plot1 = value1;
        plot2 = value2;
        return triseccion(plot1,plot2);
    }
    if (value2*plot2<0){
        plot1 = value2;
        return triseccion(plot1,plot2);
    }

}
