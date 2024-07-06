double find_zero(vector<vector<double>> polys) {
    double left = polys[0][1];
    double right = polys[0][1];
    for (int i = 0; i < polys.size(); i++) {
        if (polys[i][2] > right) {
            right = polys[i][2];
        }
        if (polys[i][0] < left) {
            left = polys[i][0];
        }
    }
    return (-left / right);
}