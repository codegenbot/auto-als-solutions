```cpp
double find_zero(vector<vector<double>> polys) {
    double left = polys[0][1];
    double right = polys[0][2];
    for (int i = 1; i < polys.size(); i++) {
        double a = polys[i][1] - polys[i-1][1];
        double b = polys[i][2] - polys[i-1][2];
        left += a;
        right *= polys[i][0] / polys[i-1][0];
    }
    return (-left) / right;
}