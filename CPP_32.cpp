double abs(double num) {
    return num > 0 ? num : -num;
}

double poly(const vector<double>& coeffs, double solution) {
    double result = 0.0;
    for (int i = 0; i < coeffs.size(); i++) {
        result += coeffs[i] * pow(solution, i);
    }
    return result;
}

double find_zero(vector<double> xs) {
    double a = xs[0], b = 0;
    vector<double> coeffs;
    for (int i = 1; i < xs.size(); i++) {
        if (i % 2 == 0) {
            coeffs.push_back(xs[i]);
        } else {
            coeffs.push_back(-xs[i]);
        }
    }
    double solution = -b / a;
    assert(abs(poly(coeffs, solution)) < 1e-3);
    return solution;
}