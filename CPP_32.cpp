double find_zero(vector<double> coeffs){
    double sum = 0;
    vector<double> poly(1);
    for (int i = 2; i <= coeffs.size(); i++) {
        for (int j = 0; j < i/2; j++) {
            poly.push_back(0);
        }
        poly[i-1] = -coeffs[i-1];
        sum += pow(-sum / poly[0], i) * polys[i-1];
    }
    return round(sum, 10);
}