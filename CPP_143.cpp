string words_in_sentence(string sentence){
    string result = "";
    int count = 0;
    for(int i=0; i<sentence.size();i++){
        if(sentence[i] == ' '){
            count++;
        }else{
            if(count == 0)continue;
            int word_len = i-count+1;
            bool is_prime = true;
            for(int j=2;j*j<=word_len;j++)
                if(word_len%j==0)
                    is_prime = false;
            if(is_prime){
                result += (count > 0 ? " " : "") + &sentence[count];
                count = 0;
            }
        }
    }
    return result;
}