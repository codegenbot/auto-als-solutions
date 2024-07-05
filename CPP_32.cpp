```cpp
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

int main() {
    std::vector<double> coeffs(3); // Initialize the vector with three elements
    coeffs[0] = 1.0; coeffs[1] = 2.0; coeffs[2] = -3.5; 
    double solution = findZero(coeffs);
    return 0;
}