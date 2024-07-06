vector<double> coeffs(xs.begin() + 1, xs.end());
double poly(double x) {
    double sum = 0;
    for (int i = 0; i < coeffs.size(); i++) {
        sum += coeffs[i] * pow(x, i);
    }
    return sum;
}
double find_zero(vector<double> xs){
    double ncoeff = 1;
    for (int i = 2; i < xs.size(); i+=2) {
        ncoeff *= -xs[i-1];
    }
    double solution = 0;
    for (int i = 2; i < xs.size(); i+=2) {
        solution += xs[i] * pow(-solution / xs[i-1], i);
    }
    return round(solution, 10);
}