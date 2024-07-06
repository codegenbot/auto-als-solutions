double find_zero(vector<double> xs){
    int n = xs.size();
    double solution;
    for(int i=1; i<n; i++){
        double a = 0;
        for(int j=0; j<i; j++)
            a += xs[j] * pow(1.0, i-j);
        if(a == 0) return 1.0;
    }
    solution = -xs[1]/2*xs[2];
    while (abs((int)polynomial(xs, solution)) > 1e-3){
        solution = (solution + polynomial(xs, solution)/polyDerivative(xs, solution));
    }
    return solution;
}

double polynomial(vector<double> xs, double x){
    int n = xs.size();
    double p = 0.0;
    for(int i=0; i<n; i++)
        p += xs[i] * pow(x, i);
    return p;
}

double polyDerivative(vector<double> xs, double x){
    int n = xs.size();
    double p = 0.0;
    for(int i=1; i<n; i++)
        p += i*xs[i-1] * pow(x, i-1);
    return p;
}