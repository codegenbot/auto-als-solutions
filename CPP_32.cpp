double find_zero(vector<double> coeffs) {
    double left = 0;
    double right = 1;
    double zero = -1;

    for (int i = 2; i < coeffs.size(); i++) {
        if ((coeffs[i] * left - coeffs[i-1]) * (coeffs[i] * right - coeffs[i-1]) < 0) {
            zero = min({zero, (right + left) / 2.0});
        }
        else if ((coeffs[i] * left - coeffs[i-1]) == 0) {
            return left;
        }
        else {
            if (coeffs[i] * left - coeffs[i-1] > 0) {
                right = left;
            }
            left = (coeffs[i] * left - coeffs[i-1]) / coeffs[i];
        }
    }

    return zero;
}