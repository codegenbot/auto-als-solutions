double find_zero(vector<double> xs){
    int n = xs.size();
    double a = xs[0];
    for(int i=1; i<n; i++){
        a = 0;
        for(int j=0; j<i; j++)
            a += xs[j] * pow(1.0, i-j);
        if(a == 0) return 1.0;
    }
    double solution = -xs[1]/2*xs[2];
    assert (abs((int)polynomial(xs, solution))< 1e-3);
    return solution;
}