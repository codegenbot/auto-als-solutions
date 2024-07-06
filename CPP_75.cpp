Here is the solution:

bool is_multiply_prime(int a){
    for(int i=2; i<=100; i++){
        int count = 0;
        for(int j=2; j<=i/2; j++){
            if(i%j==0)count++;
        }
        if(count==1)return true;
    }
    return false;
}