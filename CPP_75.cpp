Here is the completed code:

bool is_multiply_prime(int a){
    for(int i=2; i<=a/3; i++){
        bool prime = true;
        for(int j=2; j*j <= i; j++){
            if(i%j == 0) prime = false;
        }
        if(prime) {
            int b = a/i;
            int c = a/b;
            if(c*b==a && is_prime(b) && is_prime(c)) return true;
        }
    }
    return false;
}

bool is_prime(int n){
    if(n<=1) return false;
    for(int i=2; i*i <= n; i++){
        if(n%i == 0) return false;
    }
    return true;
}