string solve(int N){
    int sum = 0;
    while(N > 0) {
        int remainder = N % 2;
        sum += remainder;
        N /= 2;
    }
    string result = "";
    while(sum > 0) {
        if (sum & 1)
            result = "1" + result;
        else
            result = "0" + result;
        sum >>= 1;
    }
    return result;
}