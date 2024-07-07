string words_in_sentence(string sentence){
    string result = "";
    int count = 0;
    for(int i=0; i<sentence.size(); i++){
        if(sentence[i] == ' '){
            count++;
            continue;
        }
        bool isPrime = true;
        for(int j=2; j*j<=count+1; j++){
            if((count+1)%j==0){
                isPrime = false;
                break;
            }
        }
        if(isPrime) result += sentence.substr(i-count, count)+ " ";
        count++;
    }
    return result;
}