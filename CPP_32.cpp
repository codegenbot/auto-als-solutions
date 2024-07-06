double find_zero(vector<double> coeffs, vector<double> xs){
    double left = xs[0];
    double right = xs[xs.size() - 1];
    for(int i=0; i<coeffs.size(); i++){
        if(coeffs[i] == 0) continue;
        left *= 1.0/coeffs[i];
        right *= 1.0/coeffs[i];
    }
    return (-left / right);
}