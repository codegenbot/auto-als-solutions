#include <cmath>
#include <vector>
#include <cassert>
#include <ostream>

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

    assert(abs(poly(coeffs, solution))< 1e-3);

    cout << "The zero of the polynomial is: " << solution << endl;
    return 0;
}