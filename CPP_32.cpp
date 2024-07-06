double find_zero(vector<double> xs){
    double sum = 0;
    for(int i=1; i<xs.size();i+=2){
        sum += (-1) * xs[i]/(double)i * pow(xs[0], (double)(i-1));
    }
    return -sum;
}