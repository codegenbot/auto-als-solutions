int prod_signs(vector<int> arr){
    int product = 1;
    long long sum = 0;

    for(int i : arr){
        if(i == 0) {
            return -32768; // empty array
        }
        product *= (i > 0 ? 1 : ((i < 0) ? -1 : 0));
        sum += abs(i);
    }

    return (sum * product);
}