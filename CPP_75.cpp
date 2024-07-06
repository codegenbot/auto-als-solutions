Here's the completed code:

bool is_multiply_prime(int a){
    for(int i=2; i<=a; i++){
        bool prime=true;
        for(int j=2; j<=i/2; j++){
            if(i%j==0)prime=false;break;
        }
        if(prime && a%i==0) return true;
    }
    return false;
}