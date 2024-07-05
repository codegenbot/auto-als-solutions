#include <cmath>
#include <vector>

double polyZero(std::vector<double> coeffs) {
    double a = coeffs[0];
    double b = 0;
    for(int i=1; i<coeffs.size(); i+=2) {
        b += coeffs[i];
    }
    return -b / (2*a);
}

int main() {
    std::vector<double> coeffs = {1.0, -7.0, 12.0, -6.0}; 
    double solution = polyZero(coeffs);

    return 0;
}