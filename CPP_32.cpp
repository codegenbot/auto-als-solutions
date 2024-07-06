vector<double> coeffs = xs;
double poly(vector<double> coeffs, double x) {
    int n = coeffs.size();
    double result = 0;
    for(int i=0; i<n; i++)
        result += coeffs[i] * pow(x, i);
    return result;
}