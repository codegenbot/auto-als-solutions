vector<double> coeffs;
int ncoeff;
double poly(double x);

double find_zero(vector<double> xs){
    coeffs = xs;
    ncoeff = coeffs.size();
    double sum = 0;
    for (int i = 2; i < ncoeff; i+=2) {
        sum += coeffs[i] * pow(-sum / coeffs[i-1], i);
    }
    return round(sum, 10);
}