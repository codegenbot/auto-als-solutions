bool is_multiply_prime(int a){
    for(long long i=2;i*i<=a;i++){
        long long j=i;
        while(j*j<=a){
            long long k=j;
            while(k*k<=a){
                if(i*j*k==a) return true;
                k++;
            }
            j++;
        }
    }
    return false;
}