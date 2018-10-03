#include <iostream>


using namespace std;


#include <math.h>

double iterative(double, int);
int main()
{

cout<<"RAIZ DE 7: "<<sqrt(7);
cout<<" \nUTILIZANDO SEMILLA = 2.00000 -> las iteraciones son: "<<iterative(2.00000,0);
return 0;

}



double iterative(double y, int n){
if (y == sqrt(7)){
return n;
}
else{
y= (y+(7/y))/2;
n++;
cout<<"\niteracion = "<<n<<" valor = "<<y;
return iterative(y,n);
}
}
