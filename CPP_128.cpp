Here is the solution:

int prod_signs(vector<int> arr){
    long long product = 1;
    long long sum = 0;
    for(int i: arr){
        if(i < 0) product *= -1;
        else if(i > 0) product *= 1;
        sum += abs(i);
    }
    return product * (sum == 0) ? -32768 : sum;
}