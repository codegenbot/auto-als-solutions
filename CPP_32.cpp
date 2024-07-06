vector<double> coeffs;
int ncoeff;
double poly(double x) {
    double sum = 0;
    for (int i = 0; i < ncoeff; i++) {
        sum += coeffs[i] * pow(x, i);
    }
    return sum;
}
double find_zero(vector<double> xs){
    int ncoeff = xs.size();
    vector<double> coeffs(xs.begin(), xs.end());
    double solution = 0;
    for (int i = 2; i < ncoeff; i+=2) {
        solution += coeffs[i] * pow(-solution / coeffs[i-1], i);
    }
    return round(solution, 10);
}