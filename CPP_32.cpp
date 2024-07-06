double find_zero(vector<vector<double>> coeffs, vector<double> xs){
    double left = 0;
    double right = 0;
    double zero = 0;

    for(int i=0; i<coeffs.size(); i++){
        left += coeffs[i][0] * pow(xs[0], i);
        right += coeffs[i][1] * pow(xs[0], i);
    }

    return (-left / right);
}