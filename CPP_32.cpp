#include <cmath>
#include <vector>

double polyZero(std::vector<double> coeffs, double x0){
    int n = coeffs.size();
    double a = coeffs[0];
    double b = 0;
    
    for(int i=1; i<n; i+=2) {
        b += coeffs[i];
    }
    
    for(int i=1; i<=n/2; i++){
        x0 -= (b/(2*a));
    }
    
    return x0;
}

int main() {
    std::vector<double> coeffs = {1.0, -7.0, 12.0, -6.0}; 
    double solution = polyZero(coeffs, 0);
    
    return 0;
}