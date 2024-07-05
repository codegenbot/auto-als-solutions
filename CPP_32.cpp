#include <cmath>
#include <vector>

double findZero(std::vector<double> coeffs){
    double a = coeffs[0];
    double b = 0;
    for(int i=1; i<coeffs.size(); i+=2) {
        b += coeffs[i];
    }
    return -b / (2*a);
}

int main() {
    std::vector<double> coeffs = {1.0, -7.0, 12.0, -6.0}; 
    double solution = findZero(coeffs);

    // Initialize polyValue
    double polyValue = 0;
    for(int i=0; i<coeffs.size(); i++) {
        if(i % 2 == 0) {
            polyValue += coeffs[i] * std::pow(solution, i);
        }
    }

    assert (abs(polyValue)< 1e-3);

    return 0;
}