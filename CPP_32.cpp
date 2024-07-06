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
    double x = xs[1];
    for (int i = 2; i < xs.size(); i+=2) {
        while (true) {
            if (poly(x) == 0) {
                break;
            } else if (poly(x) * poly(xs[i]) > 0) {
                x -= 0.1;
            } else {
                x += 0.1;
            }
        }
    }
    return round(x, 10);
}