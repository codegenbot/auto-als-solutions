double find_zero(vector<double> xs){
    int n = xs.size();
    double solution;
    for(int i=1; i<n; i++){
        solution = 0;
        for(int j=0; j<i; j++)
            solution += xs[j] * pow(1.0, i-j);
        if(solution == 0) return 1.0;
    }
    solution = -xs[1]/2*xs[2];
    assert (abs((int)poly(xs, solution))< 1e-3); 
    return solution;
}