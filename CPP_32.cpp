```cpp
vector<double> coeffs;
double find_zero(vector<double> xs){
    double sum = 0;
    vector<double> poly(4);
    for (int i = 2; i < xs.size(); i+=2) {
        sum += xs[i] * pow(-sum / xs[i-1], i);
    }
    return round(sum, 10);
}

int main() {
    vector<double> coeffs = {1.0, 3.0, -5.0, 4.0}; 
    double solution = find_zero(coeffs); 
    vector<double> poly = {1.0, 2.0, 3.0, 4.0}; 
    assert(abs(poly[0] + poly[1]*solution + poly[2]*pow(solution, 2) + poly[3]*pow(solution, 3)) < 1e-3);
}