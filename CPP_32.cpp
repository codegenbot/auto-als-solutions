double find_zero(vector<double> xs){
    double sum = 0;
    vector<double> coeffs(xs.begin(),xs.end()); // define the coefficients
    for (int i = 2; i < xs.size(); i+=2) {
        sum += coeffs[i] * pow(-sum / coeffs[i-1], i);
    }
    return round(sum, 10);
}