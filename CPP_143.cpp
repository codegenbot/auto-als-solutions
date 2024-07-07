```c++
#include <iostream>
#include <string>

std::string words_in_sentence(std::string sentence) {
    std::string result = "";
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
        if(isPrime) result += sentence.substr(i-count, 1)+ " ";
        count++;
    }
    return result;
}

int main() {
    std::string word;
    word = words_in_sentence("here is");
    assert(word == "is");
    return 0;
}