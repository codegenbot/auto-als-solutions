```cpp
#include <cmath>
#include <vector>

double findZero(std::vector<double> polys){
    double a = polys[0];
    double b = 0;
    for(int i=1; i<polys.size(); i+=2) {
        b += polys[i];
    }
    return -b / (2*a);
}

int main() {
    std::vector<double> polys = {1.0, 2.0, -3.5};
    double solution = findZero(polys);
    assert(abs(solution - poly(polys, solution)) < 1e-3); 
    return 0;
}
double poly(std::vector<double> polys, double x){
    double result = polys[0];
    for(int i=1; i<polys.size(); i++) {
        result += polys[i] * pow(x, i);
    }
    return result;
}