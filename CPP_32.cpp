#include <cmath>
#include <vector>

double findZero(std::vector<double> xs){
    double a = xs[0];
    double b = 0;
    for(int i=1; i<xs.size(); i++) {
        if(i%2 == 0) { 
            b += xs[i]; 
        } else { 
            a = xs[i]; 
        }
    }
    return -b / (2*a);
}

int main() {
    std::vector<double> coeffs = {1.0, 2.0, -3.5}; 
    double solution = findZero(coeffs);
    return 0;
}