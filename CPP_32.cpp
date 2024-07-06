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
    coeffs = xs;
    double x = 1.0;
    for (int i = 2; i < ncoeff; i+=2) {
        x = -poly(x) / poly(1);
    }
    return round(x, 10);
}