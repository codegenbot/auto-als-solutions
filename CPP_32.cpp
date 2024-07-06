double find_zero(vector<double> xs) {
    vector<double> coeffs(xs.size());
    double left = xs[0];
    double right = xs[xs.size() - 1];
    for(int i=0; i<xs.size(); i++) {
        coeffs[i] = (i+1)*left + right;
    }
    return (-left / right);
}