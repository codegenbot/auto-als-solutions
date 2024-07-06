```cpp
vector<double> coeffs(xs);
int ncoeff = xs.size();
double poly(double x) {
    double result = 0;
    for (int i = 0; i < ncoeff; i++) {
        result += coeffs[i] * pow(x, i);
    }
    return result;
}
double find_zero(vector<double> xs){
    double sum = 0;
    for (int i = 2; i < xs.size(); i+=2) {
        sum += xs[i] * pow(-sum / xs[i-1], i);
    }
    return round(sum, 10);
}