long long double_the_difference(vector<double> lst){
    long long sum = 0;
    for(auto x : lst){
        if(x > 0 && x == int(x)){
            sum += pow(int(x), 2);
        }
    }
    return sum;
}