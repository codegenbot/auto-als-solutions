int sum_squares(vector<float> lst){
    int sum = 0;
    for(auto x : lst){
        double ceil_val = ceil(x);
        sum += pow(ceil_val, 2);
    }
    return static_cast<int>(sum);
}