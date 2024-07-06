string words_in_sentence(string sentence){
    string result = "";
    int len;
    for(int i=0; ispace(sentence[i]); i++){
        sentence.erase(0,i);
        len = 0;
        for(int j=i;j<length(sentence);j++)
            if(!isalpha(sentence[j])){
                len++;
                break;
            }
            else
                len++;

        bool isPrime = true;
        if(len > 1){
            for(int k=2;k*k<=len;k++){
                if(len % k == 0){
                    isPrime = false;
                    break;
                }
            }

            if(isPrime)
                result += sentence.substr(i, len) + " ";
        }
    }

    return result;
}