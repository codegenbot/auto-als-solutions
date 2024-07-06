double find_zero(vector<double> xs){
    if(xs.size() % 2 != 0 || abs(xs[0]) < 1e-6) return -1; 
    double x = (-xs[1]/xs[3]); 
    double fractional_part = modf(x, &x);
    if(fractional_part > 0.005 || fractional_part < -0.005) x += fractional_part;
    return round(x*100.0)/100.0; 
}