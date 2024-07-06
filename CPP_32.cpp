double find_zero(vector<double> xs){
    double sum = 0;
    for (int i = 2; i < xs.size(); i+=2) {
        sum += xs[i] * pow(-sum / xs[i-1], i);
    }
    return round(sum, 10);
}