string solve(int N){
    int sum = 0;
    while(N > 0) {
        int digit = N & 1;
        if(digit) sum++;
        N >>= 1;
    }
    return to_binary(sum);
}

string to_binary(int n) {
    string res = "";
    while(n > 0) {
        res = (n & 1 ? "1" : "0") + res;
        n >>= 1;
    }
    return res;
}