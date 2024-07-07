#include <string>

int words_in_sentence(string sentence) {
    int result = 0;
    int count = 1;
    for(int i=0; i<sentence.size(); i++){
        if(sentence[i] == ' '){
            int word_length = i - count;
            bool isPrime = true;
            for(int j=2; j*j<=word_length+1; j++){
                if((word_length)%j==0){
                    isPrime = false;
                    break;
                }
            }
            if(isPrime) result++;
            count = i + 1;
        }
    }
    return result;
}