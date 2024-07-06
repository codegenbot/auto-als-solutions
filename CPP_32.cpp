double find_zero(vector<double> xs){
    int n = xs.size();
    double solution;
    for(int i=1; i<n; i++){
        solution = xs[0];
        for(int j=1; j<=i; j++)
            solution += xs[j] * pow(1.0, i-j);
        if(abs((int)solution)< 1e-3) return 0.0;
    }
    return solution;
}