vector<double> coeffs(3); // Initialize coefficients array
coeffs[0] = xs[1];
coeffs[1] = (xs[2] - xs[0]) / 2;
coeffs[2] = xs[0];

double poly(double x) {
    return coeffs[2] + coeffs[1]*(x-0.5) + coeffs[0]*pow(x-0.5, 2);
}

int ncoeff = coeffs.size();