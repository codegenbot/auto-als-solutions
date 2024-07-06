int sum_squares(vector<float> lst){
    int result = 0;
    for(auto x : lst){
        result += ceil(x)*ceil(x);
    }
    return result;
}