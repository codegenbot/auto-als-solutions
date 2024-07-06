vector<int> even_odd_count(int num) {
    vector<int> result(2);
    int n = abs(num);
    while(n){
        if(n%10%2) {
            result[1]++;
        } else {
            result[0]++;
        }
        n /= 10;
    }
    return result;
}