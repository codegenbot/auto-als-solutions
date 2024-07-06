double find_zero(vector<double> xs){
    vector<double> coeffs(xs.size());
    double left = 0;
    double right = 0;
    
    for(int i=0; i<xs.size(); i++){
        if(i==0) left = xs[i];
        else if(i==xs.size()-1) right = xs[i];
    }
    
    return (-left / right);
}