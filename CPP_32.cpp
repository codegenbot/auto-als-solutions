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
    if(xs.size() % 2 != 0) return -1; // Only works with even number of coefficients
    double max_coeff = abs(xs[0]);
    for(int i=1; i<xs.size();i++){
        if(abs(xs[i]) > max_coeff) max_coeff = abs(xs[i]);
    }
    double x = -max_coeff;
    while(poly(xs, x) != 0){
        x += 0.01;
    }
    return x;
}