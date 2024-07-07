#include <string>

int words_in_sentence(string sentence){
    int result = 0;
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
        if(isPrime) result += 1;
        count++;
    }
    return result;
}