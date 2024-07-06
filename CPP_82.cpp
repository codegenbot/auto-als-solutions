bool prime_length(string str){
    int len = str.length();
    if(len <= 1) return true; // 0 and 1 are considered prime lengths
    for(int i = 2; i*i <= len; i++){
        if(len % i == 0) return false;
        while(len % (i*2) == 0){
            len /= (i*2);
        }
    }
    return true;
}