#include <cmath>
#include <vector>
#include <iostream>
using namespace std;

double poly(vector<double> coeffs, double solution) {
    double result = coeffs[0];
    for(int i=1; i<coeffs.size(); i++) {
        if(i%2==0)
            result += coeffs[i] * pow(solution, (i/2));
        else
            result += coeffs[i] * pow(solution, ((i-1)/2));
    }
    return result;
}

double findZero(vector<double> coeffs){
    double a = coeffs[0];
    double b = 0;
    for(int i=1; i<coeffs.size(); i+=2) {
        b += coeffs[i];
    }
    return -b / (2*a);
}

int main() {
    vector<double> coeffs = {1.0, -7.0, 12.0, -6.0}; 
    double solution = findZero(coeffs);

    cout << "Solution: " << solution << std::endl;
    cout << "Polynomial value at the solution: " << poly(coeffs, solution) << std::endl;

    return 0;
}