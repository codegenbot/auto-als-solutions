string words_in_sentence(string sentence){
    string result = "";
    for(int i=0; i<sentence.size(); i++){
        if(i > 0 && sentence[i-1] == ' '){
            int len = 1;
            while(i+len <= sentence.size() && sentence[i+len] != ' ') 
                len++;
            if(isPrime(len)){
                result += sentence.substr(i, len) + " ";
            }
            i += len - 1;
        }
    }
    return result;
}

bool isPrime(int n){
    if(n <= 1) return false;
    for(int i = 2; i * i <= n; i++) 
        if(n % i == 0) return false;
    return true;
}