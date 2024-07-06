#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;

double poly(vector<double> xs, double x){
    double sum=0;
    int i;
    for (i=0;i<xs.size();i++)
    {
        sum+=xs[i]*pow(x,i);
    }
    return sum;
}

double find_zero(vector<double> xs){
    if(xs.size() % 2 != 0)
        return -1; // invalid input: number of coefficients must be even
    double x = 1.0; // initial guess for the root
    double y = poly(xs, x);
    while(abs(y) > 1e-6){ // loop until the result is close enough to zero
        x -= y/poly({(double)i*x for i in range(xs.size())},x); // Newton-Raphson method
        y = poly(xs, x);
    }
    return x;
}