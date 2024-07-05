double find_zero(vector<double> xs){
    double root = 1;
    for(int i=1; i<xs.size();i+=2) {
        root = -xs[i]/(i*root);
    }
    return round(root, 10);
}