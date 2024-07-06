double find_zero(vector<double> xs){
    double a = xs[0], b = 0;
    for (int i = 1; i < xs.size(); i++) {
        b += (i % 2 == 0) ? xs[i] : -xs[i];
    }
    return -b / a;
}