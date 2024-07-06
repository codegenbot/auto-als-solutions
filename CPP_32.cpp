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
    if(xs.size() % 2 != 0 || abs(xs[0]) < 1e-6) return -1; // Check for even number of coefficients and largest non zero coefficient
    double x = (-xs[1]/xs[3]); 
    return round(x, 2);
}