double find_zero(vector<vector<double>> polys) {
    vector<double> coeffs;
    double left = 0, right = 0;
    for (const auto& poly : polys) {
        double x = 1;
        double sum = 0;
        for (int i = poly.size() - 1; i >= 0; --i) {
            sum += poly[i] * pow(x, i);
        }
        if (sum > 0) right = x;
        else left = x;
    }
    return (-left / right);
}