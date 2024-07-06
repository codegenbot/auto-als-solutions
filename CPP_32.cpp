```
vector<double> coeffs = xs;
double find_zero(vector<double> xs){
    int n = xs.size();
    double a = 0;
    for(int i=0; i<n; i++){
        a = 0;
        for(int j=0; j<=i; j++)
            a += coeffs[j] * pow(1.0, i-j);
        if(a == 0) return 1.0;
    }
    double x = -coeffs[1]/2*coeffs[2];
    return x;
}
double poly(vector<double> coeffs, double x){
    int n = coeffs.size();
    double a = 0;
    for(int i=0; i<n; i++)
        a += coeffs[i] * pow(x, i);
    return a;
}