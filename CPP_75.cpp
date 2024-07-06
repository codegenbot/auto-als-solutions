bool is_multiply_prime(int a){
    for(long long i=2; i*i<=a; i++){
        if(a%i==0){
            long long j=i;
            while(j*j<=a) {
                if(a%j==0 && is_prime(j)) {
                    int k=a/j;
                    if(is_prime(k) && is_prime(i))
                        return true;
                }
                j++;
            }
        }
    }
    return false;
}

bool is_prime(int n){
    if(n<2)
        return false;
    for(int i=2; i*i<=n; i++){
        if(n%i==0)
            return false;
    }
    return true;
}