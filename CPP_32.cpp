vector<double> coeffs;
double find_zero(vector<double> xs){
    vector<double> poly = {1.0};
    double sum = 0;
    for (int i = 2; i < xs.size(); i+=2) {
        vector<double> newPoly;
        for(int j=0;j<poly.size();j++){
            newPoly.push_back(poly[j]);
        }
        newPoly.push_back(0);
        newPoly.back() += -sum / xs[i-1] * poly.back();
        sum = 0;
        poly = newPoly;
    }
    return round(sum, 10);
}