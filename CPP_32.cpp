```
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
    std::vector<double> coeffs;
    coeffs.push_back(1.0);
    coeffs.push_back(2.0);
    coeffs.push_back(-3.5);
    double solution = findZero(coeffs);
    assert(std::abs(coeffs[0] + coeffs.size() * solution - 0) < 1e-3); 
    return 0;
}