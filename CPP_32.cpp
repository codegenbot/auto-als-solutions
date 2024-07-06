double find_zero(vector<double> coeffs){
    double sum = 0;
    vector<double> poly(1);
    for (int i = 0; i < coeffs.size(); i++) {
        if(i % 2 == 0) {
            poly.push_back(coeffs[i]);
        } else {
            for(int j = 0; j <= i/2; j++) {
                poly[j] += (-1) * pow(poly, i);
            }
        }
    }
    return round(poly[0], 10);
}