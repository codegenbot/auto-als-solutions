#include <string>

int words_in_sentence(string sentence){
    int result = 0;
    int count = 1;
    for(int i=0; i<sentence.size(); i++){
        if(sentence[i] == ' '){
            count++;
            continue;
        }
        bool isPrime = true;
        for(int j=2; j*j<=count; j++){
            if((count)%j==0){
                isPrime = false;
                break;
            }
        }
        if(isPrime) result++;
        count++;
    }
    return result;
}