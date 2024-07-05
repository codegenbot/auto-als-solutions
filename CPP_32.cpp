```cpp
#include <cmath>
#include <vector>

double findZero(std::vector<double> coeffs) {
    double a = coeffs[0];
    double b = 0;
    for(int i=1; i<coeffs.size(); i+=2) {
        b += coeffs[i];
    }
    return -b / (2*a);
}

int main() {
    std::vector<double> coeffs;
    double x;
    int n;

    std::cout << "Enter the number of coefficients: ";
    std::cin >> n;

    coeffs.resize(n);

    std::cout << "Enter the coefficients:\n";
    for(int i = 0; i < n; ++i) {
        std::cout << "Enter coefficient for x^" << (n - 1 - i) << ": ";
        std::cin >> coeffs[i];
    }

    double solution = findZero(coeffs);

    // Define poly function to calculate polynomial value
    double polyValue = 0;
    for(int i=0; i<coeffs.size(); i++) {
        if(i % 2 == 0) {
            polyValue += coeffs[i] * std::pow(solution, i);
        }
    }

    assert (abs(polyValue)< 1e-3);

    return 0;
}