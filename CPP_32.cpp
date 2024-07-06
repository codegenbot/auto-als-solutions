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
    double x = -1.0; // Initial guess
    double tol = 1e-6; // Tolerance for convergence

    while(true) {
        double p = poly(xs, x); // Evaluate polynomial at current x
        if (abs(p) < tol) { // Check for convergence
            return x;
        }
        x -= p / poly({xs[0], 1}, x); // Update x using Newton's method
    }
}