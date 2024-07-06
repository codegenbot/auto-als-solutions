double find_zero(vector<double> xs){
    int n = xs.size();
    double solution = 0;
    for(int i=n-1; i>=0; i--){
        solution += xs[i] * pow(1.0, n-i-1);
    }
    for(double x=-10; x<=10; x+=0.01){
        if(abs((int)polynomial(xs, x))< 1e-3) return x;
    }
    return -1;
}

double polynomial(vector<double> coeffs, double solution){
    double result = 0;
    int n = coeffs.size();
    for(int i=0; i<n; i++){
        result += coeffs[i] * pow(solution, n-i-1);
    }
    return result;
}