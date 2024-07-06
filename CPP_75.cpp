bool is_prime(int n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

bool is_multiply_prime(int a){
    bool prime[100] = {false};
    for(int i=2; i<100; i++){
        if(!prime[i]){
            for(int j=i*2; j<100; j+=i){
                prime[j] = true;
            }
        }
    }
    int temp = a;
    while(temp > 1){
        if(!is_prime(temp)) return false;
        for(int j=2; temp > 1;j++){
            if(temp%j == 0){
                temp /= j;
                break;
            }
            else {
                temp--;
            }
        }
    }
    return true;
}