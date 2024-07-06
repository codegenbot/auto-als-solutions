bool prime_length(string str){
    int len = str.length();
    bool is_prime = true;

    for(int i = 2; i * i <= len && is_prime; i++){
        if(len % i == 0) is_prime = false;
    }

    return is_prime;
}