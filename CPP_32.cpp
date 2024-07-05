int main() {
    vector<double> coeffs = {1.0, -7.0, 12.0, -6.0}; 
    double solution = findZero(coeffs);

    assert(abs(poly(coeffs, solution))< 1e-3);

    return 0;
}