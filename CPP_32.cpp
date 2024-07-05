#include <cmath>
#include <vector>

double findZero(std::vector<double> xs){
    double a = xs[0];
    double b = 0;
    for(int i=1; i<xs.size(); i+=2) {
        b += xs[i];
    }
    return -b / (2*a);
}

// Define the polynomial function
double poly(std::vector<double> coeffs, double x){
    double result = 0;
    for(int i=0; i<coeffs.size(); i++){
        result += coeffs[i] * pow(x, i);
    }
    return result;
}

int main() {
    std::vector<double> coeffs = {1.0, 2.0, -3.5}; 
    double solution = findZero(coeffs);
    // Check if the solution is correct
    assert (abs(poly(coeffs, solution))< 1e-3);
    return 0;
}