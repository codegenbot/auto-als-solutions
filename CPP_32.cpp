```cpp
#include <cmath>
#include <vector>

double findZero(std::vector<double> coeffs){
    double a = coeffs[0];
    double b = coeffs[1];
    double c = 0;
    for(int i=2; i<coeffs.size(); i++) {
        c += coeffs[i];
    }
    return -b/(2*a) - (c+pow(b, 2)/(4*a)) / (2*a);
}

int main() {
    std::vector<double> coeffs = {1.0, -3.5}; 
    double solution = findZero(coeffs);
    return 0;
}