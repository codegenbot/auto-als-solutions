vector<double> coeffs;
double find_zero(vector<double> xs){
    double sum = 0;
    vector<double> poly(xs.begin(),xs.end()); // define the polynomial
    for (int i = 2; i < xs.size(); i+=2) {
        sum += xs[i] * pow(-sum / xs[i-1], i);
    }
    return round(sum, 10);
}

int main() {
    vector<double> coeffs = {1.0, 3.0, -5.0, 4.0}; // define the coefficients
    double solution = find_zero(coeffs); // call the function
    assert(abs(coeffs[0] + coeffs[1]*solution + coeffs[2]*pow(solution,2) + coeffs[3]*pow(solution,3)) < 1e-3);
}