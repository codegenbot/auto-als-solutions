bool is_multiply_prime(int a){
    bool prime[100] = {false};
    for(int i=2; i<100; i++){
        if(!prime[i]){
            for(int j=i*2; j<100; j+=i){
                prime[j] = true;
            }
        }
    }
    for(int i=2; a > 1; ){
        while(a % i == 0) {
            a /= i;
            i++; // <--- Add this line!
        }
    }
    return true;
}