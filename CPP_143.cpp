string words_in_sentence(string sentence){
    string result = "";
    int primeCount = 0;
    
    for(int i=2; i<=sentence.size(); i++){
        bool isPrime = true;
        for(int j=2; j*j <= i; j++){
            if(i % j == 0){
                isPrime = false;
                break;
            }
        }
        if(isPrime) primeCount++;
        
        if(primeCount > 0 && (sentence.size() - primeCount < i || primeCount == sentence.size())){
            result += sentence + " ";
            primeCount--;
        }
    }
    
    return result.substr(0, result.find(" "));
}