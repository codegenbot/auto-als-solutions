```
vector<double> coeffs = xs;
double poly(vector<double> coeffs, double x) {
    double result = 0.0;
    for(int i=0; i<coeffs.size(); i++) {
        result += coeffs[i] * pow(x, i);
    }
    return result;
}

double find_zero(vector<double> xs){
    vector<double> coeffs = xs;
    int n = coeffs.size();
    double a = 1.0;
    for(int i=1; i<n; i++){
        a = 0;
        for(int j=0; j<i; j++)
            a += coeffs[j] * pow(1.0, i-j);
        if(a == 0) return 1.0;
    }
    double x = -coeffs[1]/2*coeffs[2];
    return x;
}