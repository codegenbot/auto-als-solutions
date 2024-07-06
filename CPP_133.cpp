Here is the completed code:

int sum_squares(vector<float> lst){
    int sum = 0;
    for(float i : lst){
        int ceil_i = ceil(i);
        sum += pow(ceil_i,2);
    }
    return sum;
}