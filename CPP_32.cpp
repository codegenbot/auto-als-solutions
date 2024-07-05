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
    std::vector<double> polys = {1.0, 2.0, -3.5};
    double solution = findZero(polys);
    assert(std::abs(polys[1] + polys.size() * solution - 0) < 1e-3); 
    return 0;
}